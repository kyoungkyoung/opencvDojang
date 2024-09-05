import cv2, sys
import numpy as np

# 트랙바 콜백함수
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'red_result')
    hmax = cv2.getTrackbarPos('H_max', 'red_result')
    
    # inRange 함수에 적용
    # dst = cv2.inRange(src_hsv, (hmin,150,0), (hmax,255,255))
    # cv2.imshow('Trackbar', dst)
    
    # 색상 특정하기
    red_result = cv2.inRange(red_hsv, (hmin,150,0), (hmax,255,255))
    cv2.imshow('red_result', red_result)
    


redLight = cv2.imread('data2/red.jpg')
yellowLight = cv2.imread('data2/yellow.jpg')
greenLight = cv2.imread('data2/green.jpg')

if redLight is None:
    sys.exit('Image load failed')

# 각 이미지 색상의 범위 지정 bgr->hsv
red_hsv = cv2.cvtColor(redLight, cv2.COLOR_BGR2HSV)
yellow_hsv = cv2.cvtColor(yellowLight, cv2.COLOR_BGR2HSV)
green_hsv = cv2.cvtColor(greenLight, cv2.COLOR_BGR2HSV)

# 창 생성
cv2.namedWindow('red_result')
cv2.namedWindow('yellow_result')
cv2.namedWindow('green_result')

cv2.imshow('red_result', redLight)
cv2.imshow('yellow_result', yellow_hsv)
cv2.imshow('green_result', green_hsv)

# 색상 특정하기
red_result = cv2.inRange(red_hsv, (0,150,0), (5,255,255))
cv2.imshow('red_result', red_result)

yellow_result = cv2.inRange(yellow_hsv, (10,50,0), (30,255,255))
cv2.imshow('yellow_result', yellow_result)

green_result = cv2.inRange(green_hsv, (64,50,0), (72,255,255))
cv2.imshow('green_result', green_result)


# cv2.createTrackbar('H_min', 'red_result', 0, 255, on_trackbar)
# cv2.createTrackbar('H_max', 'red_result', 0, 255, on_trackbar)


cv2.waitKey()
cv2.destroyAllWindows()