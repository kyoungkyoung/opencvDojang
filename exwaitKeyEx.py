# import cv2, sys
# import numpy as np

# # 화살표를 누르면 원이 이동되는 어플

# # 변수 초기화
# width, height = 512, 512

# # 초기 원의 좌표
# x, y, R = 256,256, 50

# direction = 0

# # main
# while(True):
    
#     # 빈 흰 캔버스 생성
#     img = np.zeros((width, height, 3), np.uint8)+255
    
#     # 원을 그린다. img에 (x,y)좌표에 반지름 R로, 빨간색으로 안을 채워서(-1)
#     cv2.circle(img, (x,y), R, (0,0,255), -1)
#     cv2.imshow('img', img)
    
    
    
#     # 방향키와 같은 특수한 키의 입력을 받을 때는 waitKey()가 아니라 waitKeyEx()를 사용
#     # rlqhs waitKey + Extention키 입력까지 받아들임
#     key = cv2.waitKeyEx(30) #timeout = 30ms
#     if key == 27: #ESC
#         break
#     elif key == 0x270000: # right key
#         direction = 0
#         x+=10
#     elif key == 0x280000: # down key
#         direction = 1
#         y+=10
#     elif key == 0x250000: # left key
#         direction = 2
#         x-=10
#     elif key == 0x260000: # up key
#         direction = 3
#         y-=10
        
    
    
# cv2.destroyAllWindows()






import cv2, sys
import numpy as np

# 화살표를 누르면 원이 이동되는 어플
width, height = 512, 512

#초기에 원의 좌표와 반지름
x,y,R = 256, 256, 50

direction = 0

# main
while True:
    # 빈 흰 캔버스 생성
    img = np.zeros((width, height, 3), np.uint8)+255
    # 원을 그린다. img에 (x,y)좌표에, 반지름R로, 빨간색으로 안을 채워서-1
    cv2.circle(img, (x,y), R, (0,0,255), -1)
    cv2.imshow('img', img)    
    
    # 기본 waitKey + Extention키 입력까지 받아들임
    key = cv2.waitKeyEx(30)  #timeout=30ms
    
    # 종료 조건
    if key == 27: #ESC
        break
    # right key
    elif key ==0xF703:
        direction =0
        x+=10
    # down key
    elif key ==0xF701:
        direction =1
        y+=10
    # left key
    elif key ==0xF702:
        direction =2
        x-=10
    # up key
    elif key ==0xF700:
        direction =3
        y-=10
    

    
    
cv2.destroyAllWindows