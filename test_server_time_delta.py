# grpc server
from grpc_server.task_server_thread import GetClientStub
from grpc_server import task_pb2


# data processing
import time
import numpy as np
import pandas as pd

# constant
time_delta_test_rounds = 100000
test_rounds = 50000
server1 = 'server'
server2 = 'ubantu21'
writer_path = server1 + '_to_' + server2 + 'net_delay.xlsx'
grpc_ip = '192.168.40.133'
grpc_port = 10000

if __name__ == "__main__":
    # get grpc client
    client_stub = GetClientStub(grpc_ip, grpc_port)
    delta_time = []

    for test_round in range(1, time_delta_test_rounds+1):
        if test_round % 100 == 0:
            print(test_round/100)
        start_request_time = time.time()
        arrival_time = float(client_stub.server_time_delta(task_pb2.TimeDeltaRequest()).arrival_time)
        end_request_time = time.time()
        delta_time.append((end_request_time+start_request_time)/2 - arrival_time)
    
    average_time_delta = np.mean(np.array(delta_time))
    print(server1 + ' and ' + server2 + 'time_delta:{}'.format(average_time_delta))

    time_data = {}
    for test_round in range(1, test_rounds+1):
        if test_round % 1000 == 0:
            print('网络延迟测试：'+str(test_round/100))
        start_request_time = time.time()
        arrival_time = float(client_stub.server_time_delta(task_pb2.TimeDeltaRequest()).arrival_time)
        time_data[test_round] = {}
        time_data[test_round]['test_round'] = test_round
        time_data[test_round]['start_request_time'] = start_request_time
        time_data[test_round]['arrival_time'] = arrival_time

    df = pd.DataFrame(data=time_data).T
    df['net_delay'] = df['arrival_time'] + average_time_delta - df['start_request_time']
    writer = pd.ExcelWriter(writer_path)
    df.to_excel(writer, index=False)
    writer.save()
    writer.close()