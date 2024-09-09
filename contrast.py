# cv2.normalize

import cv2, sys
import numpy as np

src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
# .shape : 이걸로 채널이 몇개인지 확인 -> 컬러면 3개, 
#          cv2.IMREAD_GRAYSCALE -> 이건 채널 1개 -> 단일채널
# print(src.shape)

if src is None:
    sys.exit('Image load failed')
    

# src이미지에서 최소값과 최대값을 확인 (pixMin, pixMax)
# minMaxLoc의 return 값이 4개인데, 앞에 2개는 받고, 뒤에 2개는 받지 않고 싶을 때, 받지 않고 싶은 리턴값은 _(언더바)로 표기
pixMin, pixMax, _, _ = cv2.minMaxLoc(src)
print('dfdfdfdf')
print(pixMin, pixMax)

# 1. dst값을 =으로 받을때는 2번째 파라미터를 None으로 줘서 return값을 받고,                                        
# 2. dst값을 2번째 파라미터 값으로 받을 수 있다 -> 첫번째 인자인 src값을 두번째 인자인 dst값으로 넘겨주는것
# normalize()는 리턴값을 받는 방법이 두가지!
# 이미지를 정규화 한다.
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
pixMin, pixMax, _, _ = cv2.minMaxLoc(dst)
print(pixMin, pixMax)

cv2.imwrite('data2/Hawkes_norm.jpg', dst)
cv2.imshow('img', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
