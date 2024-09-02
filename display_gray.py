# plt.imshow함수에서 interpolation 옵션
# cmap은 이미지가 컬러일 경우 cmap 지정을 안해도 컬러로 출력
# cmap = "gray"

import cv2, sys
from matplotlib import pyplot as plt

fileName = 'data/cat.jpg'
imgGray = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray', interpolation='bicubic') #colormap 은 gray
plt.show()



# 채널이 뭐징....
# 데이터 시각화 -> 마크와 채널
# 마크(mark) : 점, 선, 면으로 이루어진 기본 데이터 시각화 요소
# 채널(channel) : 마크를 변경할 수 있는 요소들, 마크에 뜻을 추가해주는 요소들