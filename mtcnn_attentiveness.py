import math


def receive_coordinate(boxes_c, landmarks):
    weight = [0, 0]
    # print("test", landmarks)
    for i in range(landmarks.shape[0]):
        lefteyes_coordinate = (int(landmarks[i][2 * 0]), int(landmarks[i][2 * 0 + 1]))
        righteyes_coordinate = (int(landmarks[i][2 * 1]), int(landmarks[i][2 * 1 + 1]))
        nose_coordinate = (int(landmarks[i][2 * 2]), int(landmarks[i][2 * 2 + 1]))
        for j in range(len(landmarks[i]) // 2):
            # 中心点坐标
            print("centre", (int(landmarks[i][2 * j]), int(int(landmarks[i][2 * j + 1]))))
        a = ((nose_coordinate[0] - righteyes_coordinate[0]) ** 2 +
             (nose_coordinate[1] - righteyes_coordinate[1]) ** 2)
        b = ((nose_coordinate[0] - lefteyes_coordinate[0]) ** 2 + (
                nose_coordinate[1] - lefteyes_coordinate[1]) ** 2)
        c = ((righteyes_coordinate[0] - lefteyes_coordinate[0]) ** 2 + (
                righteyes_coordinate[1] - lefteyes_coordinate[1]) ** 2)
        k1 = float(b) / float(a)
        print("a=", a, " b=", b, " c=", c)
        cosC = (a + b - c) / (2 * (a ** 0.5) * (b ** 0.5))
        print("cosC = ", cosC)
        k2 = math.acos(cosC)
        if k1 > 1.24 or k1 < 0.86:
            # 不专注
            print("不专注")
            weight[0] = 0
        else:
            # 专注
            print("专注")
            weight[0] = 1

        if k2 > 66 or k2 < 0:
            print("不专注")
            weight[1] = 0
        else:
            print("专注")
            weight[1] = 1
        print("test", weight)
        return weight
