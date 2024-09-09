import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')
    
# 1. 사용자 커널(=필터)을 생성해서 blur
# filter2D(src, -1, kernel) : 입력이미지, ddepth, 필터값 을 넣어줌
kernel = np.ones((3,3), dtype=np.float32)/9
mask1 = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
dst = cv2.filter2D(src, -1, kernel)
dst1 = cv2.filter2D(src, -1, mask1)

# 2. blur kernel을 사용해서
dst2 = cv2.blur(src, (3,3))

cv2.imshow('img', src)
cv2.imshow('dst', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()