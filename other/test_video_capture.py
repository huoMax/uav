#video handle
import cv2

# import
import sys
sys.path.append("..")

# img handle
from tools.img_handle import CreateVideoCapture
from tools.img_handle import DestroyVideoCapture

test_video = "30-minutes.mp4"

if __name__ == "__main__":
    # 建立窗口, 窗口名为 'Window'
    # cv2.namedWindow('Window', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
    
    # cap = CreateVideoCapture()
    cap = cv2.VideoCapture()
    cap.open(test_video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(test_video + " frame count: {}, fps: {}".format(frame_count, fps))
    # # 逐帧显示捕获的视频流, 若按下 ‘q’则退出捕获
    # while(True):
    #     ret, frame = cap.read()  #第一个参数返回一个布尔值（True/False），代表有没有读取到图片；第二个参数表示截取到一帧的图片
    #     if ret:
    #         cv2.imshow('Window', frame)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
                
    # cv2.destroyAllWindows()
    DestroyVideoCapture(cap)