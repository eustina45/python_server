# 레이블 감지 코드

import boto3

def detect_labels_local_file(photo):

    client = boto3.client('rekognition') 

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})   

    result = []

    for label in response["Labels"]:
        name = label["Name"]
        confidence = label["Confidence"]

        result.append(f"{name} : {confidence:.2f}%")

    r = "<br/>".join(map(str, result))
    return r


# 얼굴 비교 코드

def compare_faces(sourceFile, targetFile):
    client = boto3.client('rekognition')
    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')
    response = client.compare_faces(SimilarityThreshold=0,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})
    
    result = []
    
    for faceMatch in response['FaceMatches']:
        similarity = faceMatch['Similarity']
        
    imageSource.close()
    imageTarget.close()

    return f"동일 인물일 확률은{similarity:.2f}%입니다"