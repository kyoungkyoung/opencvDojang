import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

isColor = True
if not isColor:
    src1 = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('data2/Hawkes_norm.jpg', cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        sys.exit('Image load failed')

    # 히스토그램 만들기
        # .calcHist(): 이미지를 읽어서 히스토그램으로 만들어 주는 함수
        # 0-256을 256칸으로 각각 나눠서 보여줘
        # calcHist([src1], [0], None, [128], [0,256]) -> 0-256을 128칸으로 나눠서 보여줘 -> 픽셀을 2개씩 묶어서 그 그룹의 값이 히스토그램으로 나옴
    hist = cv2.calcHist([src1], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([src2], [0], None, [256], [0,256])

if isColor:
    src1 = cv2.imread('data/lena.bmp')
    
    if src1 is None:
        sys.exit("Image Load failed")
    
    # 컬러 채널 분리
    colors = ['b', 'g', 'r'] # matplotlib에서 사용되는 그래프 색상
    bgr_planes = cv2.split(src1)  #<class 'tuple'> -> 튜플클래스로 리턴
    print(len(bgr_planes[0])) #512,512,512 

    for (p, c) in zip(bgr_planes, colors):
        hist = cv2.calcHist([p],[0],None,[256],[0,256])
        plt.plot(hist, color=c)



cv2.imshow('src1', src1)
# cv2.imshow('src2', src2)
# matplotlib 띄우기
# plt.plot(hist)
# plt.plot(hist2)

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()