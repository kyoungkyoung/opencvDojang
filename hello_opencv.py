import sys
import cv2

# opencv 버전 확인
print('Hello OpenCV', cv2.__version__)

# imread('파일명') -> 이미지를 읽어라
# img의 데이터 타입은 numpy.ndarray
img_gray = cv2.imread('data/Lena2.jpg', cv2.IMREAD_GRAYSCALE) # 흑백
img_bgr = cv2.imread('data/Lena2.jpg') # default 는 컬러
print(type(img_bgr))
print(cv2.imread('data/Lena2.jpg'))
print(cv2.IMREAD_GRAYSCALE) # 1

# 파일을 못찾아서 이미지를 못읽어온 경우 프로그램 종료
# 반드시 예외처리를 해주자
if img_gray is None or img_bgr is None:
    print('Image load failed!')
    sys.exit()

# 창의 이름('image')을 정의
cv2.namedWindow('image_gray')
cv2.namedWindow('image_bgr')

# 불러온 이미지를 창에 띄워준다
# 'image'창에 읽어온 img 배열을 출력한다.
cv2.imshow('image_gray', img_gray)
cv2.imshow('image_bgr', img_bgr)

# 키입력을 기다리는 함수
# 함수 안에 값을 입력 -> 단위 : ms -> 1000ms = 1s
# waitKey() 함수에 지연값을 설정하지 않으면 키보드 입력이 들어올때까지 무한 대기
cv2.waitKey(1000)

# 모든 창을 다 닫는다.
cv2.destroyAllWindows()