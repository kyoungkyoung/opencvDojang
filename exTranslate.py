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

def rotate(src, rad):
    aff = np.array([[np.cos(rad), np.sin(rad), 0],\
                    [-np.sin(rad), np.cos(rad), 0]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (0,0)) # 이미지 창을 더 넓은 부분까지 보고 싶다면 마지막 튜플값 변경 (0,0) -> (100,100)
    
    return dst
    
def rotate2(src, angle):
    h, w = src.shape[:2]
    # 좌표값은 튜플로 저장
    centerPt = (w/2, h/2) 

    # getRotationMatrix2D가 알아서 변환행렬(affine matrix)을 만들어줌
    # 센터좌표, 로테이션 앵글, 스케일을 그대로 1
    aff = cv2.getRotationMatrix2D(centerPt, angle, 1)
    dst = cv2.warpAffine(src, aff, (w,h))
    
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
# dst = rotate(src, rad)
dst = rotate2(src, angle)



cv2.imshow('src', src)
cv2.imshow('dst', dst)
# cv2.imshow('INTER_CUBIC', dst1)
# cv2.imshow('INTER_NEAREST', dst2)
# cv2.imshow('INTER_LANCZOS4', dst3)

cv2.waitKey()
cv2.destroyAllWindows()