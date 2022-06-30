import time
import pandas as pd 

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
file_name = 'single_node_test.xlsx'

if __name__ == "__main__":
    time_record = []
    cap = CreateVideoCapture()
    writer = pd.ExcelWriter(file_name)


    #进行 10 次测试, 每次递增100张图片
    for i in range(10):
        # path_folder = "img/" + str((i+1)*100) + "/"
        # 进行图片处理，记录每次处理前后时间
        for j in range((i+1)*100):
            ret, frame = cap.read()
            if ret:
                time_start = time.time()
                success, frame_out = APIFaceRecognition(frame, "wgk", j)
                time_end = time.time()
                # cv2.imwrite(path_folder+str(j)+".jpg", frame_out)
                time_record.append([time_start, time_end, time_end - time_start])
        
        # 记录实验数据
        df = pd.DataFrame({
            'start_time':[time_start for time_start, time_end, cost_time in time_record],
            'end_time':[time_end for time_start, time_end, cost_time in time_record],
            'cost_time':[cost_time for time_start, time_end, cost_time in time_record]
            })
        time_record = []
        sheet_name = str((i+1)*100) + "-single_node" + "-" + host_name
        df.to_excel(writer, sheet_name= sheet_name)

    writer.save()
    writer.close()
    
    DestroyVideoCapture(cap)