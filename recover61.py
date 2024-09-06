import cv2, sys
import numpy as np

hmin = 50
hmax = 70

# 트랙바 콜백함수 생성
def on_trackbar(pos):
    global hsv, hmin, hmax
    
    hmin = cv2.getTrackbarPos('H_min', 'frame')
    hmax = cv2.getTrackbarPos('H_max', 'frame')
    
    # inRange 함수에 적용
    # mask = cv2.inRange(hsv,(hmin,150,0),(hmax,255,255))
    # cv2.copyTo(frame2, mask, frame1)
    # cv2.imshow('frame', frame1)

# 동영상 파일명
fileName1 = 'data2/woman.mp4'
fileName2 = 'data2/raining.mp4'

# 영상 불러오기
cap1 = cv2.VideoCapture(fileName1)
cap2 = cv2.VideoCapture(fileName2)

if not cap1.isOpened():
    # print('vedio1 open failed')
    sys.exit('vedio1 open failed')
    
    
if not cap2.isOpened():
    sys.exit('vedio2 opend failed')
    
# 동영상의 fps 확인
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))

print(fps1) # 23
print(fps2) # 25

# 동영상의 총 프레임
frameCount1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frameCount2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

# 초당 몇 프레임? -> 1번 동영상 기준
delay = int(1000/fps1)

# 합성 여부 설정 플래그
do_composite = False


# 트랙바를 추가하기 위해 창을 먼저 생성
cv2.namedWindow('frame')

# 트랙바 추가 ( H_min : 40 ~ 60 )
cv2.createTrackbar('H_min', 'frame', 40, 60, on_trackbar)
cv2.createTrackbar('H_max', 'frame', 60, 80, on_trackbar)
# on_trackbar(0)

ret1, frame1 = cap1.read()
hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break
    
    if do_composite:
        ret2, frame2 = cap2.read()
        if not ret2:
            break
    
        # hsv 색공간에서 영역을 검출해서 합성
        # h : hue (색상)
        # s : saturation (채도) -> 색이 진한정도
        # v : value (명도)
        # h,s,v 각각 1byte
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        # h: 50-70, s: 150-255, v: 0-255
        # inRange() : 이미지의 특정 색상 범위를 추출하는 데 사용
        # inRange(): 범위안에 있다면 범위 안에 있는 것만 골라낸다
        mask = cv2.inRange(hsv,(hmin,150,0),(hmax,255,255))
        cv2.copyTo(frame2, mask, frame1)
    
    
    

    
    
    
    
    
    # 결과 확인
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)
    
    # 스페이스바를 눌렀을 때 do_composite를 반전
    if key==ord(' '):
        do_composite = not do_composite
    
    # ESC가 입력되면 종료
    elif key==27:
        break
    
cap1.release()
cap2.release()
cv2.destroyAllWindows()
