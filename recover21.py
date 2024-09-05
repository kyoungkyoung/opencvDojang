# 이미지를 불러올때는 imread()
# 동영상을 불러올때는 VideoCapture()

import cv2, sys

fileName = 'data/vtest.avi'

# VideoCapture 클래스 객체 생성 + 생성자 호출(파일열기)
cap = cv2.VideoCapture(fileName)

# 동영상의 해상도 width, height, frame 수를 확인
frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),\
      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),\
      int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

# print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

#768.0 -> pixel값은 실수가 될 필요가 없기 때문에 명시적형변환 int()를 해줌
print(frameSize)


# 동영상 이미지를 다 가져올때까지 반복
while(True):
    # .read()
    # 동영상에서 한장의 이미지를 가져오기
    # retval : 동영상에서 이미지 가져올 때 정상 동작 했니? -> True / False
    # frame : 이미지 한장
    # 동영상 코덱 디코딩도 포함
    retval, frame = cap.read()
    
    # retval(리턴값)이 False인 경우 if문 실행
    if not retval:
        break
    
    # 보여줘라
    cv2.imshow('frame', frame)
    
    # 100ms 대기 (이 동영상은 초당 10프레임 짜리 이니까)
    # 프레임: 동영상을 구성하는 개별적인 정지 이미지
    key = cv2.waitKey(100)
    
    # 키 입력이 ESC(27)이면 종료
    if key == 27:
        break
    
# 동영상을 열었으면, 닫아라 -> 반드시! -> 이걸 안해주면 나중에 기록이 멈춘다.
if cap.isOpened():
    cap.release() # 열림 해제
    
cv2.destroyAllWindows()