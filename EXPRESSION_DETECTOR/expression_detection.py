import cv2
from deepface import DeepFace


img=cv2.imread("C:\\Users\\abine\\Desktop\\old\\IMG20211224122525.jpg")
result=DeepFace.analyze(img,actions=['emotion'])
value=result[0]["dominant_emotion"]
print(value)
cv2.putText(img,"EMOTION:"+value,(10,40),cv2.FONT_ITALIC,1,(6,7,34),3)
cv2.imshow('Emotion_detector',img)
cv2.waitKey(0)


