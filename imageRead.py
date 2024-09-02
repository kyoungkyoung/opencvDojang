# 파일에서 이미지를 읽어서 출력

import cv2
import sys

fileName = "data/cat.jpg"

# 이미지 불러오기
img = cv2.imread(fileName)
print(img.shape)

# 예외처리 루틴 : 이미지를 불러오지 못했을 때 -> 반드시 예외처리를 해줘야 함
if img is None:
    print("Image load fail")
    # 프로그램 종료
    sys.exit()
    
# 창에 이미지를 출력
# 창의 이름을 img
cv2.namedWindow('img')

# img창에 Img배열을 출력
cv2.imshow('img', img)

# 키보드 입력을 기다리는 함수
# inKey = cv2.waitKey()
# print(inKey)

# 이미지 배열을 파일로 저장하는 함수
# png 파일로 저장
cv2.imwrite('cat.png', img)

# jpg 파일로 저장
cv2.imwrite('cat1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 85])
# 화질이 높게 손실율을 적게 설정
cv2.imwrite('cat2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95])

# 'q' 키를 눌렀을 때 창이 종료되게
loop = True
while(loop):
    inKey = cv2.waitKey()
    print(inKey)
    if inKey == ord('q'):
        print('왜 안오냐고오오오오오오')
        # img 창만 닫기
        cv2.destroyWindow('img')
        loop = False

# 모든 창 닫기
# cv2.destroyAllWindows()