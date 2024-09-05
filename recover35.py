import cv2, sys

# VideoCapture() 클래스 객체 생성
cap = cv2.VideoCapture(0)

print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),\
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),\
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    retval, frame = cap.read() # 프레임 캡처 if not retval:
    if not retval:
        break

    cv2.imshow('frame',frame)

    key = cv2.waitKey(25)
    if key == 27: # Esc 
        break
# 25/1000 sec 대

if cap.isOpened():
    cap.release()
