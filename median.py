import cv2, sys
import numpy as np

src = cv2.imread('data2/noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit("Image load failed")
    
# threshold를 잘 조절하면 내가 원하는 범위를 설정 할 수 있다.
# Canny Edge Detector는 기본적으로 그레이스케일화된 이미지만을 처리한다.
# dst에서 threshold값은 64와 128
# 이 값들로 임계값을 변화시켜 엣지를 탐지 -> threshold값을 변환 시키면서 확인
dst = cv2.medianBlur(src, 3)

cv2.imshow('src',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()

