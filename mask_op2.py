import cv2, sys

# 이미지 불러오기
# img = cv2.imread('data2/opencv-logo-white.png') -> 알파채널 안나옴
logo = cv2.imread('data2/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
src = cv2.imread('data2/cat.bmp')

# 모든 행, 모든 열 0-2번 채널
logo = logo[:,:,0:3]
# print(img.shape)

# 알파채널만 슬라이싱
mask = logo[:,:,3]
# print(mask.shape)

# mask의 영역
h,w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]



# 마스크 연산
cv2.copyTo(logo, mask, crop)
cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()



