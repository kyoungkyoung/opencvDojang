import cv2, sys
import numpy as np

ptRec = []
ptTri = []

# 원, 다각형 그리고 파일 저장
def mouse_callback(event, x, y, flags, param):
    global ptRec, ptTri
    canvas = param[0]
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            
            # 사각형 그리기
            if len(ptRec) < 4:
                ptRec.append([x,y])
                print(ptRec)
            # 삼각형 그리기
            elif len(ptTri) < 3:
                ptTri.append([x, y])
                print(ptTri)
                
        print(len(ptRec), len(ptTri))
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(canvas, (x, y), 30, (0,255,0), 1)
    
    # 삼각형,사각형 그리기
    if len(ptRec) == 4 and len(ptTri) == 3:    
        cv2.polylines(canvas, [np.array(ptRec), np.array(ptTri)], isClosed=True, color = (255,0,0)) 
    
    # 그린 화면 업데이트
    cv2.imshow('canvas', canvas)
    
    # 파일로 저장
    cv2.imwrite('misson/0909.jpg', canvas)

def mkCanvas():
    # 흰색 캔버스 생성
    canvas = np.zeros((512,512,3), np.uint8)+255
    cv2.namedWindow('canvas')

    # 마우스 콜백함수로 그리기
    cv2.setMouseCallback('canvas', mouse_callback, [canvas])
    cv2.imshow('canvas', canvas)

    exitKey = cv2.waitKey()
    if exitKey == 27:
        cv2.destroyAllWindows()
        

# 리사이징후 선 얼마나 뭉개지는지 관찰
img = cv2.imread('misson/0909.jpg')
print(img.shape)

# 리사이징함수 이용 - 확대
dst1_cubic = cv2.resize(img, (0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
dst2_nearest = cv2.resize(img, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst3_lanczos4 = cv2.resize(img, (0,0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)

# cv2.imshow('dst1_cubic', dst1_cubic)
# cv2.imshow('dst2_nearest', dst2_nearest)
# cv2.imshow('dst3_lanczos4', dst3_lanczos4)

# 리사이징함수 이용 - 축소
dst1_cubic_s = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
dst2_nearest_s = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST) #선이 안나오는군!
dst3_lanczos4_s = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('dst1_cubic_s', dst1_cubic_s)
cv2.imshow('dst2_nearest_s', dst2_nearest_s)
cv2.imshow('dst3_lanczos4_s', dst3_lanczos4_s)

# 블러처리
kernel_size = 3
ksize = (kernel_size, kernel_size)

dst_blur = cv2.blur(img, ksize)
cv2.imshow('dst_blur', dst_blur)

# 블러처리 후 리사이징함수 이용 - 축소
dst1_cubic_bs = cv2.resize(dst_blur, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
dst2_nearest_bs = cv2.resize(dst_blur, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST) #선이 안나오는군!
dst3_lanczos4_bs = cv2.resize(dst_blur, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('dst1_cubic_bs', dst1_cubic_bs)
cv2.imshow('dst2_nearest_bs', dst2_nearest_bs)
cv2.imshow('dst3_lanczos4_bs', dst3_lanczos4_bs)






cv2.waitKey()
cv2.destroyAllWindows()
