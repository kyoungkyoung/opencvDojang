import cv2, sys
import numpy as np
import math

def translate(src, x_move=0, y_move=0):
    
    # 이미지의 이동 변환 => x -> 200, y->100만큼 이동
    # 얼마나 이동하고 싶은지 -> 단위행렬 1,0,0,1 말고 그 옆에 1행은 x축 이동, 2행은 y축 이동
    h, w = src.shape[:2]
    aff = np.array([[1,0,x_move],
                    [0,1,y_move]], dtype=np.float32)
    # 변환후에 출력되는 배열의 크기 (입력되는 src 이미지의 크기를 그대로 출력)
    dst = cv2.warpAffine(src,aff, (h+y_move,w+x_move))
    print(dst.shape)
    
    return dst

    
def shear(src, x_shear=0, y_shear=0):
    if x_shear>0 and y_shear == 0:
        aff = np.array([[1, x_shear, 0][0,1,0]], dtype=np.float32)
        h,w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, (w + int(h * x_shear), h)) 
    
    elif y_shear > 0 and x_shear  == 0:
        aff = np.array([[1, 0, 0][y_shear,1,0]], dtype=np.float32)
        h,w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, w,  int(w * y_shear))   
    
    return dst   

def scale(src, x_scale, y_scale):
    h, w = src.shape[:2]
    aff = np.array([[x_scale,0,0],[0,y_scale,0]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (int(w*x_scale), int(h*y_scale)))
    return dst


'''
2x3 어파인 변환 행렬
일반적으로 2D 이미지의 어파인 변환에 사용되는 2x3 행렬은 다음과 같은 구조를 가집니다.
[ a, b, c ]
[ d, e, f ]
Use code with caution.
a, b, d, e: 회전, 크기 조정, 기울이기 등의 변환을 담당합니다.
c, f: 이동(translation)을 담당합니다.
회전만 고려하는 경우
회전만을 위한 어파인 변환 행렬은 다음과 같이 간소화됩니다.
[ cos(θ), sin(θ), 0 ]
[ -sin(θ), cos(θ), 0 ]
Use code with caution.
θ: 회전 각도를 나타냅니다.


cv2.getRotationMatrix2D(center, angle, scale) 함수는 위 과정을 자동으로 처리하여, 
지정한 center 좌표를 중심으로 회전하는 어파인 변환 행렬을 생성합니다.
제공해주신 코드에서 별도의 이동 (c, f) 없이 회전만 수행하기 때문에 원점을 중심으로 이미지가 회전하는 것입니다.
원하는 지점을 중심으로 회전시키려면 cv2.getRotationMatrix2D 함수를 사용하거나,
직접 어파인 변환 행렬을 구성할 때 이동 성분을 추가해야 합니다.

rotate 함수는 회전 중심을 이미지의 좌측 상단으로 고정하고 회전하기 때문에, 회전된 이미지의 일부가 잘릴 수 있습니다.
rotate2 함수는 회전 중심을 이미지의 중심으로 설정하여 회전하기 때문에, 이미지 전체가 보존됩니다.
cv2.warpAffine 함수의 dsize 파라미터를 조정하여 출력 이미지의 크기를 변경할 수 있습니다.
예를 들어, (src.shape[1] * 2, src.shape[0] * 2)를 입력하면 가로와 세로 크기가 두 배로 커집니다.


'''










def rotate(src, rad):

    aff = np.array([[np.cos(rad), np.sin(rad), 100],\
                    [-np.sin(rad), np.cos(rad), 200]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (1000,1000)) # 이미지 창을 더 넓은 부분까지 보고 싶다면 마지막 튜플값 변경 (0,0) -> (100,100)
    
    return dst

def rotate2(src, angle):
    h, w = src.shape[:2]
    # 좌표값은 튜플로 저장
    centerPt = (w/2, h/2) 

    # getRotationMatrix2D가 알아서 변환행렬(affine matrix)을 만들어줌
    # 센터좌표, 로테이션 앵글, 스케일을 그대로 1
    aff = cv2.getRotationMatrix2D(centerPt, angle, 1)
    dst = cv2.warpAffine(src, aff, (w*2,h*2))
    
    return dst
    
src = cv2.imread('data2/rose.bmp')

if src is None:
    sys.exit('Image load failed')
    

print(src.shape)
# dst = translate(src, 50,50) # 이미지 이동 변환
# dst = shear(src, 0.5,0)
# dst = scale(src, 1.5, 1.5)
# 512x512 -> 1024x1024
# dst = cv2.resize(src,(1024,1024))
# 비율로 설정 -> 해상도 입력X
# dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
# dst2 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
# dst3 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)

# 각도를 라디안으로 변환하는 공식
# 왼쪽 상단이 중심점
angle = 20
rad = angle*math.pi/180
dst = rotate(src, rad)
# dst = rotate2(src, angle)



cv2.imshow('src', src)
cv2.imshow('dst', dst)
# cv2.imshow('INTER_CUBIC', dst1)
# cv2.imshow('INTER_NEAREST', dst2)
# cv2.imshow('INTER_LANCZOS4', dst3)

cv2.waitKey()
cv2.destroyAllWindows()