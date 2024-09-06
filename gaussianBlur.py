import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit("Image load failed")
    
# blur처리
# 필터의 크기가 (3x3) -> 필터의 크기가(커널의 크기가) 클수록 연산량이 많아져서 시간이 오래걸림
# blur함수가 연산을 해서 list로 return

dst1 = cv2.GaussianBlur(src, (0,0), 1)
dst2 = cv2.GaussianBlur(src, (0,0), 2)
dst3 = cv2.GaussianBlur(src, (0,0), 3)

cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)

cv2.waitKey()
cv2.destroyAllWindows()