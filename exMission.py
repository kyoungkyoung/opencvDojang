import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러오기
src = cv2.imread('misson/01.png')

if src is None:
    sys.exit('Image load failed')

# 히스토그램
# 컬러채널 분리
colors = ['b','g','r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p],[0],None,[256],[0,256])
    print(hist.shape)
    # plt.plot(hist, color=c)


plt.show()


# 컬러 이미지의 brigtness를 밝게 하기 위해서는 YCbCr 채널을 활용
# BGR -> Ycbcr로 컬러스페이스 변경
src_Ycbcr = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
hist1 = cv2.calcHist([src_Ycbcr], [0], None, [256], [0,256])

# split으로 채널별로 잘라내고, Y값만으로 밝기 조절
Y, Cb, Cr = cv2.split(src_Ycbcr)

# src_Ycbcr에 normalize 적용
src_norm = cv2.normalize(src_Ycbcr, None, 0, 255, cv2.NORM_MINMAX)
Y_norm = cv2.normalize(Y, None, 0, 255, cv2.NORM_MINMAX)

hist2 = cv2.calcHist([Y_norm], [0], None, [256], [0,256])


# src_Ycbcr에 equalize 적용
# Y_equalize = cv2.equalizeHist(Y)
Y_add = cv2.add(Y, 50)


# hist3 = cv2.calcHist([Y_equalize], [0], None, [256], [0,256])
hist4 = cv2.calcHist([Y_add], [0], None, [256], [0,256])


# Y_equalize, cb, cr 채널 합치기
# src_Ycbcr_equalize = cv2.merge((Y_equalize, Cb, Cr))
src_Ycbcr_add = cv2.merge((Y_add, Cb, Cr))
# src_equalize = cv2.cvtColor(src_Ycbcr_equalize, cv2.COLOR_YCrCb2BGR)
src_equalize_add = cv2.cvtColor(src_Ycbcr_add, cv2.COLOR_YCrCb2BGR)
cv2.imshow('src_equalize', src_equalize_add)


# plt.plot(hist3)
plt.show()

cv2.waitKey()
cv2.destroyAllwindows()



# 컬러 스페이스의 값을 조정할 수 있다면 굳!!