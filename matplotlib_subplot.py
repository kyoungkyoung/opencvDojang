# 이미지를 4장 불러온다.
# 이미지 4장을 하나의 창에 띄운다.
# subplot: 하나의 창에 여러개의 그래프 같이 그리기

import cv2, sys
from matplotlib import pyplot as plt

# img 4장 불러오기
imgBGR1 = cv2.imread('data/Lena2.jpg')
imgBGR2 = cv2.imread('data/orange.jpg')
imgBGR3 = cv2.imread('data/apple.jpg')
imgBGR4 = cv2.imread('data/baboon.jpg')

if imgBGR1 is None or imgBGR2 is None or imgBGR3 is None or imgBGR4 is None:
    sys.exit("image load is failed")
    
# BGR -> RGB
imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)

# matplotlib plt.subplots로 이미지를 출력
figsize = (10,10)

# subplots()는 fig와 ax를 return
# fig : 창의 특성
# ax : 좌표 위치
fig, ax = plt.subplots(2,2, figsize=figsize)  # 2,2 짜리 출력

# 눈금 지우기
ax[0][0].axis('off')
ax[0][1].axis('off')
ax[1][0].axis('off')
ax[1][1].axis('off')

# 위치 지정
ax[0][0].imshow(imgRGB1, aspect='auto') # 0,0부분에 출력
ax[0][1].imshow(imgRGB3, aspect='auto')
ax[1][0].imshow(imgRGB4)
ax[1][1].imshow(imgRGB2)


# 각각의 이미지에 타이틀 주기
ax[0][0].set_title("lena")
ax[0][1].set_title("apple")
ax[1][0].set_title("bamboo")
ax[1][1].set_title("orange")

# 창 특성 변경
fig.canvas.manager.set_window_title("subplot : 하나의 창에 여러개의 그래프 그리기")

plt.show()