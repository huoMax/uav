import time
import pandas as pd
import cv2
import numpy as np

#video handle
import cv2

# import
import sys
sys.path.append("..")

# img handle
from tools.img_handle import CreateVideoCapture
from tools.img_handle import DestroyVideoCapture

# face recognition
from app.app_api import APIFaceRecognition

host_name = "ubnatu21"
file_name = "single_node_" + str(1) + "minutes_data.xlsx"
test_video = "1-minutes.mp4"
test

if __name__ == "__main__":
    time_record = []        # 记录一轮测试中的每一帧图片的花费时间
    time_statistic = []     # 记录每一轮测试的平均处理时间, 最低处理时间, 最高处理时间


    # 打开写入excel对象
    writer = pd.ExcelWriter(file_name)

    #进行 10 轮测试
    for i in range(10):
        key = 0     # 关键帧选取

        # 建立 VideoCapture, 打开测试视频
        cap = cv2.VideoCapture()
        cap.open(test_video)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print("开始第{}轮测试视频: {}, FPS={}, frame count={}".format(i+1,test_video, fps, frame_count))
 
        # 进行图片处理，记录每次处理前后时间
        for j in range(int(frame_count)):
            ret, frame = cap.read()
            if ret and key % 30 == 0:
                time_start = time.time()
                success, frame_out = APIFaceRecognition(frame, "ymh", j)
                time_end = time.time()
                time_record.append(time_end - time_start)
            key += 1
        
        # 统计本轮测试的平均花费时间, 最小花费时间, 最大花费时间
        average_time = np.mean(time_record)
        min_time = np.min(time_record)
        max_time = np.max(time_record)
        time_statistic.append([i+1, average_time, min_time, max_time])
        
        # 将每张图片的测试数据保存到excel文件中
        df = pd.DataFrame({
            'cost_time':time_record
            })
        time_record = []
        sheet_name = str((i+1)) + "-single_node" + "-" + host_name
        df.to_excel(writer, sheet_name= sheet_name)
        writer.save()

        DestroyVideoCapture(cap)
    
    # 记录统计数据
    sheet_name = "statistic_data"
    df = pd.DataFrame({
        "test_turns":[i for i, average_time, min_time, max_time in time_statistic],
        "average_time":[average_time for i, average_time, min_time, max_time in time_statistic],
        "min_time":[min_time for i, average_time, min_time, max_time in time_statistic],
        "max_time":[max_time for i, average_time, min_time, max_time in time_statistic]
    })
    df.to_excel(writer, sheet_name=sheet_name)

    writer.save()
    writer.close()
    