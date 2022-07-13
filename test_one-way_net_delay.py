# grpc server
from grpc_server.task_server_thread import GetClientStub
from grpc_server import task_pb2
from tools.img_handle import ImgEncode


# data processing
import time
import numpy as np
import pandas as pd
import cv2

# constant
time_delta_test_rounds = 5000
server1 = 'ubantu21'
server2 = 'raspbian4-old'
writer_path = server1 + '_to_' + server2 + '_twice_net_delay.xlsx'
grpc_ip = '192.168.31.187'
grpc_port = 10000
img_path = './test_grpc.jpg'

if __name__ == "__main__":
    img = cv2.imread(img_path)
    img_orig = ImgEncode(img, ".jpg")

    # get grpc client
    client_stub = GetClientStub(grpc_ip, grpc_port)
    time_data = {}


    for test_round in range(1, time_delta_test_rounds+1):
        if test_round % 100 == 0:
            print(str(test_round) + ": " + str(time.time()))
        start_request_time = time.time()
        replay = client_stub.twice_server_time_delta(task_pb2.FaceRecognitionRequest(sequence=test_round, img_orig=img_orig, target="wgk"))
        arrival_time = float(replay.arrival_time)
        end_request_time = time.time()

        time_data[test_round] = {}
        time_data[test_round]['start_reuqest_time'] = start_request_time
        time_data[test_round]['arrival_time'] = arrival_time
        time_data[test_round]['end_reuqest_time'] = end_request_time


    df = pd.DataFrame(data=time_data).T
    writer = pd.ExcelWriter(writer_path)
    df.to_excel(writer, index=False)
    writer.save()
    writer.close()
