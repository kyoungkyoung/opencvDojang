import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 밝기 조절은 add함수를 쓰는것과 더하는 것은 다르다.

isColor = False

if not isColor:
    
    # grayScale
    # src = cv2.imread('data/cat.jpg', cv2.IMREAD_GRAYSCALE)
    src = cv2.imread('data2/candies.png', cv2.IMREAD_GRAYSCALE)
    print(src.shape)

    # 밝기 변화
    # cv2.add -> 영상처리 함수 중의 add
    # add() : 더 밝게 해주는 함수
    dst1 = cv2.add(src, 100)
    dst2 = src + 100 # 이렇게 더해주면 밝기를 높이는게 아니라 오히려 어두워짐 -> 255를 넘을 수 없기 때문에!!
    hist1 = cv2.calcHist([src], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([dst1], [0], None, [256], [0,256])
    
if isColor:
    src = cv2.imread('data/cat.jpg')
    # 채널별로 100씩 더한다 -> 100 한번만쓰면 브로드테스트 연산이 실행됨
    # 더하는 값은 튜플로 입력 -> (100,100,100)
    dst1 = cv2.add(src,(100,100,100))
    
    
    
cv2.imshow('img', src)
cv2.imshow('dst1', dst1)

plt.plot(hist1)
plt.plot(hist2)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()