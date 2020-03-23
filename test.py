# coding: utf-8

# In[1]:


import sys
from detection.MtcnnDetector import MtcnnDetector
from detection.detector import Detector
from detection.fcn_detector import FcnDetector
from train.model import P_Net, R_Net, O_Net
import cv2
import os
import numpy as np
import train.config as config
import visualize
import mtcnn_attentiveness

# In[ ]:


test_mode = config.test_mode
thresh = config.thresh
min_face_size = config.min_face
stride = config.stride
detectors = [None, None, None]
# 模型放置位置
model_path = ['model/PNet/', 'model/RNet/', 'model/ONet']
batch_size = config.batches
PNet = FcnDetector(P_Net, model_path[0])
detectors[0] = PNet

if test_mode in ["RNet", "ONet"]:
    RNet = Detector(R_Net, 24, batch_size[1], model_path[1])
    detectors[1] = RNet

if test_mode == "ONet":
    ONet = Detector(O_Net, 48, batch_size[2], model_path[2])
    detectors[2] = ONet

mtcnn_detector = MtcnnDetector(detectors=detectors, min_face_size=min_face_size,
                               stride=stride, threshold=thresh)
out_path = config.out_path


# def transmit_landmarks():
#     boxes_c, landmarks = mtcnn_detector.detect(img)
#     return boxes_c, landmarks


# if config.input_mode == '1':
def cut_picture():
    # 选用图片
    path = config.test_dir
    print("test.py running")
    for item in os.listdir(path):
        img_path = os.path.join(path, item)
        # 防止卡顿
        cv2.startWindowThread()
        img = cv2.imread(img_path)
        boxes_c, landmarks = mtcnn_detector.detect(img)
        # print("box ",boxes_c)
        # 接口

        for i in range(boxes_c.shape[0]):
            bbox = boxes_c[i, :4]
            score = boxes_c[i, 4]
            corpbbox = [int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])]
            cutimg = img[corpbbox[1]:corpbbox[3], corpbbox[0]:corpbbox[2]]
            cv2.imwrite('picture_data/cut' + str(i) + '.jpg', cutimg)
            # 画人脸框
            cv2.rectangle(img, (corpbbox[0] - 10, corpbbox[1] - 10),
                          (corpbbox[2] + 10, corpbbox[3] + 10), (255, 0, 0), 1)
            # 判别为人脸的置信度
            cv2.putText(img, '{:.2f}'.format(score),
                        (corpbbox[0], corpbbox[1] - 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # 画关键点
        mtcnn_attentiveness.receive_coordinate(boxes_c, landmarks)

        total = visualize.facial_expresssion(boxes_c, landmarks)
        print("shape0 = ", boxes_c.shape[0])
        # for i in range(landmarks.shape[0]):
        #     for j in range(len(landmarks[i]) // 2):
        #         # 中心点坐标
        #         cv2.circle(img, (int(landmarks[i][2 * j]), int(int(landmarks[i][2 * j + 1]))), 2, (0, 0, 255))
        # cv2.imshow('im', img)
        # k = cv2.waitKey(0) & 0xFF
        # if k == 27:
        #     cv2.imwrite(out_path + item, img)
        cv2.destroyAllWindows()
        return total


if config.input_mode == '2':
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_path + 'out.mp4', fourcc, 0.005, (640, 480))
    while True:
        t1 = cv2.getTickCount()
        ret, frame = cap.read()
        f = 1
        timeF = 25
        if ret:
            boxes_c, landmarks = mtcnn_detector.detect(frame)
            t2 = cv2.getTickCount()
            t = (t2 - t1) / cv2.getTickFrequency()
            fps = 1.0 / t
            # visualize.facial_expresssion(boxes_c, landmarks)
            for i in range(boxes_c.shape[0]):
                bbox = boxes_c[i, :4]
                score = boxes_c[i, 4]
                corpbbox = [int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])]
                # cv2.imwrite('picture_data/cut' + str(i) + '.jpg', cutimg)
                # 画人脸框
                cv2.rectangle(frame, (corpbbox[0], corpbbox[1]),
                              (corpbbox[2], corpbbox[3]), (255, 0, 0), 1)
                # 画置信度
                cv2.putText(frame, '{:.2f}'.format(score),
                            (corpbbox[0], corpbbox[1] - 2),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 0, 255), 2)
                # 画fps值
            cv2.putText(frame, '{:.4f}'.format(t) + " " + '{:.3f}'.format(fps), (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            # 画关键点
            # mtcnn_attentiveness.receive_coordinate(boxes_c, landmarks)
            for i in range(landmarks.shape[0]):
                for j in range(len(landmarks[i]) // 2):
                    cv2.circle(frame, (int(landmarks[i][2 * j]), int(int(landmarks[i][2 * j + 1]))), 2, (0, 0, 255))
            a = out.write(frame)
            # cv2.imshow("result", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# cmd = 'python visualize.py'
# os.system(cmd)


# def get_capture():
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter(out_path + 'out.mp4', fourcc, 0.005, (640, 480))

# 将视频文件按照每秒一张图进行抓取图片
# file = '327A015D2A52556CEA2C90B9630221B5.mp4'
# # path = file[:file.index('.')]
# file = '3'
# if config.input_mode == '3':
def test():
    # vc = cv2.VideoCapture(0)  # 读入视频文件
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_path + 'out.mp4', fourcc, 0.005, (640, 480))
    f = 1
    i = 1
    score = 0.00

    while cap.isOpened():  # 判断是否正常打开
        rval, frame = cap.read()
        cv2.imshow("img",frame)
        timeF = 10  # 视频帧计数间隔频率
        if f % timeF == 0:  # 每隔timeF帧进行存储操作
            cv2.imwrite('picture/cut0.jpg', frame)  # 存储为图像
            i = i + 1
            print("i：" + str(i) + ',frame:' + str(f))
            try:
                score = cut_picture()
            except OSError:
                pass
            # continue
        f = f + 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # return score

    cap.release()
    out.release()
    cv2.destroyAllWindows()




