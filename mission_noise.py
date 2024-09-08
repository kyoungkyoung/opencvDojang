import cv2, sys
import numpy as np

# 이미지 로드 에러처리
def imageLoadError(file):
    if file is None:
        sys.exit("Image load failed")

# 필터 적용 - 기본
def filterList(src):
    # equal_dst = cv2.equalizeHist(img1)
    normal_dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
    bilateral_dst = cv2.bilateralFilter(src, -1,10,5)
    bright_dst = cv2.add(src,(100,100,100))
    gaussian_dst = cv2.GaussianBlur(src, (0,0), 1)
    median_dst = cv2.medianBlur(src, 3)
    
    filterList = [normal_dst, bilateral_dst, bright_dst, gaussian_dst, median_dst]
    
    return filterList

def imshowFunc(src, dst):
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    
def src1Image():
    src = cv2.imread('misson/01.png')
    imageLoadError(src)
    

    kernel = np.array([[0, -1.0, 0],
                [-1, 5, -1],
                [0.1, -1, 0]])

    img_sharpen = cv2.filter2D(src=src, ddepth=-1, kernel=kernel)
    normal_dst = cv2.normalize(img_sharpen, None, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.fastNlMeansDenoisingColored(normal_dst,None,8,8,7,21)
    bright_dst = cv2.add(dst,(5,5,5))
    
    # imshowFunc(src, median_dst)
    cv2.imshow('src', src)
    cv2.imshow('dst', bright_dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

def src2Image():
    src = cv2.imread('misson/03.png')
    imageLoadError(src)
    

    kernel = np.array([[0, -0.8, 0],
                [-1, 5, -1],
                [0.1, -1, 0]])

    img_sharpen = cv2.filter2D(src=src, ddepth=-1, kernel=kernel)
    normal_dst = cv2.normalize(img_sharpen, None, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.fastNlMeansDenoisingColored(normal_dst,None,8,8,7,21)
    bright_dst = cv2.add(dst,(20,20,20))
    
    # imshowFunc(src, median_dst)
    cv2.imshow('src', src)
    cv2.imshow('dst', bright_dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

def src3Image():
    src = cv2.imread('misson/05.png')
    imageLoadError(src)
    

    kernel = np.array([[0, -1, 0],
                [-1, 5, -1],
                [0, -1.3, 0]])

    img_sharpen = cv2.filter2D(src=src, ddepth=-1, kernel=kernel)
    normal_dst = cv2.normalize(img_sharpen, None, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.fastNlMeansDenoisingColored(normal_dst,None,8,8,7,21)
    bright_dst = cv2.add(dst,(5,5,5))
    
    # imshowFunc(src, median_dst)
    cv2.imshow('src', src)
    cv2.imshow('dst', bright_dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

def src4Image():
    src = cv2.imread('misson/misson_image01.png')
    imageLoadError(src)
    

    kernel = np.array([[0, -0.7, 0],
                [-1, 5, -1],
                [0, -1.1, 0]])

    img_sharpen = cv2.filter2D(src=src, ddepth=-1, kernel=kernel)
    normal_dst = cv2.normalize(img_sharpen, None, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.fastNlMeansDenoisingColored(normal_dst,None,5,5,7,21)
    bright_dst = cv2.add(dst,(10,10,10))
    
    # imshowFunc(src, median_dst)
    cv2.imshow('src', src)
    cv2.imshow('dst', bright_dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

def src5Image():
    src = cv2.imread('misson/misson_image03.png')
    imageLoadError(src)
    

    kernel = np.array([[0, -0.6, 0],
                [-1, 5, -1],
                [0, -1, 0]])

    img_sharpen = cv2.filter2D(src=src, ddepth=-1, kernel=kernel)
    normal_dst = cv2.normalize(img_sharpen, None, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.fastNlMeansDenoisingColored(img_sharpen,None,5,5,7,21)
    bright_dst = cv2.add(dst,(10,10,10))
    
    # imshowFunc(src, median_dst)
    cv2.imshow('src', src)
    cv2.imshow('dst', bright_dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

def src6Image():
    src = cv2.imread('misson/misson_image05.png')
    imageLoadError(src)
    

    kernel = np.array([[0, -0.5, 0],
                [-0.5, 2.8, -0.5],
                [0, -0.5, 0]])

    img_sharpen = cv2.filter2D(src=src, ddepth=-1, kernel=kernel)
    normal_dst = cv2.normalize(img_sharpen, None, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.fastNlMeansDenoisingColored(normal_dst,None,5,5,7,21)
    bright_dst = cv2.add(dst,(15,15,15))
    
    # imshowFunc(src, median_dst)
    cv2.imshow('src', src)
    cv2.imshow('dst', bright_dst)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

    

# src1Image()
# src2Image()
# src3Image()
# src4Image()
# src5Image()
# src6Image()