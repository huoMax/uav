# img and video handle
import cv2
from tools.img_handle import ImgDecode
from tools.img_handle import ImgEncode
from tools.img_handle import DestroyVideoCapture

# grpc server
from grpc_server.task_server_thread import GetClientStub
from grpc_server import task_pb2


# data processing
import pandas as pd
import numpy as np
import time
import os

# constant
video_path = 'videos/1-minutes.mp4'
host_name = 'ubantu21'
grpc_ip = '192.168.40.133'
grpc_port = 10000
test_rounds = 10
imgs_out_upper_folder = 'imgs_out/'
key = 10


if __name__ == "__main__":

    # get grpc client
    client_stub = GetClientStub(grpc_ip, grpc_port)

    for test_round in range(1, test_rounds+1):
        # 打开excel文件, 获取 writer 对象
        writer_filepath = host_name + '_' + str(test_round) + '_1minutes_netdelay.xlsx'
        writer = pd.ExcelWriter(writer_filepath)

        i = 0
        time_data = {}

        # 创建图片识别结果保存目录
        imgs_out_folder = imgs_out_upper_folder + str(test_round) + '/'
        if not os.path.exists(imgs_out_folder):
            os.makedirs(imgs_out_folder)
        
        # 获取视频流
        capture = cv2.VideoCapture()
        capture.open(video_path)
        fps = capture.get(cv2.CAP_PROP_FPS)
        frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        print("开始第{}轮测试视频: {}, FPS={}, frame count={}".format(test_round,video_path, fps, frame_count))

        # 请求 grpc server 
        for frame_sequence in range(1, int(frame_count)+1):
            ret, img_orig = capture.read()
            i = i + 1
            if ret and i == key:
                i = 0
                face_recoginition_request = task_pb2.FaceRecognitionRequest(
                    sequence=frame_sequence,
                    img_orig=ImgEncode(img_orig,'.jpg'),
                    target='wgk'
                )
                start_request_time = time.time()
                face_recoginition_replay = client_stub.task_face_recognition(face_recoginition_request)
                end_request_time = time.time()

                # 记录 grpc server 处理请求花费的各种时间
                arrival_time = face_recoginition_replay.arrival_time
                start_handle_time = face_recoginition_replay.start_handle_time
                end_handle_time = face_recoginition_replay.end_handle_time
                print(arrival_time, start_handle_time, end_handle_time)

                # 保存处理后的图片
                img_out_path = imgs_out_folder + str(frame_sequence) + '.jpg'
                img_out = ImgDecode(face_recoginition_replay.img_out)
                cv2.imwrite(img_out_path, img_out)

                # 保存时间记录
                time_data[frame_sequence] = {}
                time_data[frame_sequence]['frame_sequence'] = frame_sequence
                time_data[frame_sequence]['start_request_time'] = float(start_request_time)
                time_data[frame_sequence]['end_request_time'] = float(end_request_time)
                time_data[frame_sequence]['arrival_time'] = float(arrival_time)
                time_data[frame_sequence]['start_handle_time'] = float(start_handle_time)
                time_data[frame_sequence]['end_handle_time'] = float(end_handle_time)

        
        # 保存时间记录数据到excel表
        df = pd.DataFrame(data=time_data).T
        df.to_excel(writer, index=False)
        
        # 关闭excel文件
        writer.save()
        writer.close()

        DestroyVideoCapture(capture)


