import cv2
import os
import threading
from PyQt5.QtWidgets import QFileDialog, QLCDNumber
from PyQt5.QtGui import QImage, QPixmap
# from test import test as test, cut_picture
from test import cut_picture


# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
class Display:
    def __init__(self, ui, mainWnd):
        self.ui = ui
        self.mainWnd = mainWnd

        # 默认视频源为相机
        self.ui.radioButtonCam.setChecked(True)
        self.isCamera = True
        self.isOpen = False
        self.Attenttiveness()

        # 信号槽设置
        ui.Open.clicked.connect(self.Open)
        ui.Close.clicked.connect(self.Close)
        ui.radioButtonCam.clicked.connect(self.radioButtonCam)
        ui.radioButtonFile.clicked.connect(self.radioButtonFile)

        # 创建一个关闭事件并设为未触发
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

    def radioButtonCam(self):
        self.isCamera = True

    def radioButtonFile(self):
        self.isCamera = False

    def Open(self):
        if not self.isCamera:
            self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.mp4')
            # 线程会死锁，原因未知...
            self.cap = cv2.VideoCapture(self.fileName)
            self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)

            # th = threading.Thread(target=self.Display)
            # lock = threading.Lock()
            # th.start()
            # th.run()
            # self.Display()
            f = 1
            i = 1
            score = 0.00
            time = 1000
            while self.cap.isOpened():
                self.cap.set(cv2.CAP_PROP_POS_MSEC, int(time / 1000 * 12.333))
                time += 1000
                success, frame = self.cap.read()
                # RGB转BGR
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.ui.DispalyLabel.setPixmap(QPixmap.fromImage(img))

                if self.isCamera:
                    cv2.waitKey(1)
                else:
                    cv2.waitKey(int(1000 / self.frameRate))

                # 判断关闭事件是否已触发
                if self.stopEvent.is_set():
                    # 关闭事件置为未触发，清空显示label
                    self.stopEvent.clear()
                    self.ui.DispalyLabel.clear()
                    self.ui.Close.setEnabled(False)
                    self.ui.Open.setEnabled(True)
                    break

                timeF = 100  # 视频帧计数间隔频率
                if f % timeF == 0:  # 每隔timeF帧进行存储操作
                    cv2.imwrite('picture/cut0.jpg', frame)  # 存储为图像
                    i = i + 1
                    print("i：" + str(i) + ',frame:' + str(f))
                    try:
                        score = cut_picture()
                    except OSError:
                        print(OSError)
                        pass
                    finally:
                        self.ui.Attentiveness.display(score)
                f = f + 1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


        else:
            # 下面两种rtsp格式都是支持的
            # cap = cv2.VideoCapture("rtsp://admin:Supcon1304@172.20.1.126/main/Channels/1")
            # self.cap = cv2.VideoCapture("rtsp://admin:Supcon1304@172.20.1.126:554/h264/ch1/main/av_stream")
            self.cap = cv2.VideoCapture(0)
            # 创建视频显示线程
            th = threading.Thread(target=self.Display)
            th.start()
            # cap = cv2.VideoCapture(0)
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            # out = cv2.VideoWriter(out_path + 'out.mp4', fourcc, 0.005, (640, 480))
            f = 1
            i = 1
            score = 0.00

            while self.cap.isOpened():  # 判断是否正常打开
                rval, frame = self.cap.read()
                # cv2.imshow("img", frame)
                timeF = 100  # 视频帧计数间隔频率
                if f % timeF == 0:  # 每隔timeF帧进行存储操作
                    cv2.imwrite('picture/cut0.jpg', frame)  # 存储为图像
                    i = i + 1
                    print("i：" + str(i) + ',frame:' + str(f))
                    try:
                        score = cut_picture()
                    except OSError:
                        print(OSError)
                        pass
                    finally:
                        self.ui.Attentiveness.display(score)
                f = f + 1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    def Close(self):
        # 关闭事件设为触发，关闭视频播放
        self.stopEvent.set()
        self.isOpen = False

    def Attenttiveness(self):
        show = self.ui.Attentiveness
        show.display(0.00)
        # if self.isOpen:
        #     show.display(test(self))

    def Display(self):
        self.ui.Open.setEnabled(False)
        self.ui.Close.setEnabled(True)

        while self.cap.isOpened():
            success, frame = self.cap.read()
            # RGB转BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.ui.DispalyLabel.setPixmap(QPixmap.fromImage(img))

            if self.isCamera:
                cv2.waitKey(1)
            else:
                cv2.waitKey(int(1000 / self.frameRate))

            # 判断关闭事件是否已触发
            if self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.DispalyLabel.clear()
                self.ui.Close.setEnabled(False)
                self.ui.Open.setEnabled(True)
                break
