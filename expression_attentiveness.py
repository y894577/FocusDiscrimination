def facial_expression_recognition(score, attensiveness_weight):
    class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    angry_weight = score.data.cpu().numpy()[0] * -1
    disgust_weight = score.data.cpu().numpy()[1] * -2
    fear_weight = score.data.cpu().numpy()[2] * 0
    happy_weight = score.data.cpu().numpy()[3] * 1
    sad_weight = score.data.cpu().numpy()[4] * -1
    surprise_weight = score.data.cpu().numpy()[5] * 2
    neutral_weight = score.data.cpu().numpy()[6] * 0
    weight = angry_weight + disgust_weight + fear_weight + happy_weight + sad_weight + surprise_weight + neutral_weight
    weight = weight / len(class_names)
    class_score = 50 + 50 * weight
    if attensiveness_weight is None:
        return 0
    class_score = class_score * 0.8 + (attensiveness_weight[0] + attensiveness_weight[1]) * 10
    print("weight = ", weight)
    print("score = ", class_score)
    return class_score
