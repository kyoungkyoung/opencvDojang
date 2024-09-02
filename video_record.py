# 컨셉은 webcam에서부터 들어오는 영상을 녹화
# 비디오 파일을 열어서 사용하는 예제 먼저

import cv2, sys

isWEBCAM = True

if isWEBCAM:
    # webcam인 경우 카메라 번호를 입력
    cap = cv2.VideoCapture(0)
else :
    fileName = 'data/vtest.avi'
    cap = cv2.VideoCapture(fileName)

# 카메라의 이미지 사이즈 
frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
             int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

if isWEBCAM:
    frameSize = (int(cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)),
                 int(cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)))

print(frameSize)

# 카메라에서 전달되는 초당 프레임 수
# cv2.CAP_PROP_FPS -> 카메라에서 들어오는 이미지 프레임 속도 그대로를 저장
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 반드시 while문 밖에서 writer를 만들어줘야함
# 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 컬러 동영상 녹화를 위해
out1 = cv2.VideoWriter('myrecord0.mp4',fourcc, fps, frameSize)
# grayscale 동영상 녹화를 위해
out2 = cv2.VideoWriter('myrecord1.mp4',fourcc, fps, frameSize, isColor=False)
    
    
while(True):
    # 한 프레임 영상 읽어오기
    retval, frame = cap.read()

    # 카메라에서부터 영상이 정상적으로 전달되었는지 확인
    if not retval:
        break
    
    # 동영상 녹화기에 프레임 전달
    out1.write(frame)
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(grayFrame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', grayFrame)
    
    # 1000/fps -> delay값
    delay = int(1000/fps)
    #cv2.waitKey(delay)
    
    if cv2.waitKey(delay) == 27:
        break
    
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()