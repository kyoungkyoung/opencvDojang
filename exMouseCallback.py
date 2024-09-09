import cv2, sys
import numpy as np

# 마우스 콜백 함수 구현
# 마우스에서 이벤트가 발생하면서 호출되는 함수
# 버튼 클릭, 마우스 좌표를 이동

pt1 = (0,0)
pt2 = (0,0)



def mouse_callback(event, x, y, flags, param):
    # global img, 
    global pt1, pt2
    img = param[0]
    if event == cv2.EVENT_LBUTTONDOWN:
        # 원 그리기
        # img에 그림을 그리고, (x,y)좌표에 반지름 5, 빨간색, 선두께 3으로 원으로 그린다.
        # cv2.circle(img, (x,y), 5, (0,0,255), 3) 
        
        # 사각형 그리기
        pt1 = (x,y)
        
    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x,y)
        cv2.rectangle(img, pt1, pt2, (255,0,0), 3)
        
    # 그린 화면을 업데이트
    cv2.imshow('img', img)
'''    
    if event == cv2.EVENT_LBUTTONDOWN:
        print('LButton DOWN')
    elif event == cv2.EVENT_LBUTTONUP:
        print('LButton UP')
    elif event == cv2.EVENT_MOUSEMOVE:
        print('x:{},y:{}'.format(x,y))
'''
    
    
# 흰색 캔버스를 생성
# 행과 열의 개수가 512,512이고 3개 채널이 전부 0 또는 255인 캔버스 만들기
# img = np.zeros((512,512,3), np.uint8)+255
img = np.ones((512,512,3), np.uint8)*255
cv2.namedWindow('img')


# 메인에서 setMouseCallback 함수를 실행하면서 콜백함수를 지정
cv2.setMouseCallback('img', mouse_callback, [img])
cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()