import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('data2/rose.bmp')

if src is None:
    sys.exit("Image load failed")
    
# blur처리
# 필터의 크기가 (3x3) -> 필터의 크기가(커널의 크기가) 클수록 연산량이 많아져서 시간이 오래걸림
# blur함수가 연산을 해서 list로 return
# ksize: 흐리게 처리할 커널의 크기를 나타내는 튜플입니다. (width, height) 형태로 지정합니다.
kernel_size = 3
ksize = (kernel_size, kernel_size)

dst = cv2.blur(src, ksize)

cv2.imshow('src',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()