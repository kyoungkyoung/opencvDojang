import cv2, sys
import numpy as np
from glob import glob
import os

# 0. 파일 목록 읽기(data 폴더) *.jpg -> 리스트
# 1. 이미지 불러오기
# 2. 마우스 콜백함수 생성
# 3. 콜백함수에서 박스를 그리고, 박스 좌표를 뽑아낸다. (마우스 좌표 2개)
#    참고로 YOLO에서는 박스의 중심좌표(x,y), w,h
# 4. 이미지 파일명과 동일한 파일명으로(확장자만 떼고) txt파일 생성
# 추가 기능 0 : 박스를 잘못 쳤을 때 'c'를 누르면 현재파일의 박스 내용 초기화
# 추가 기능 1 : 화살표(->)를 누르면 다음 이미지 로딩되고(1-4)
# 추가 기능 2 : 화살표(<-)를 눌렀을 때 txt파일이 있다면 박스를 이미지 위에 띄워주면

# 이런 내용들은 개별 함수 기능으로 만드는 것이 좋다.

def getImageList():
    # 현재 작업 디렉토리 확인
    basePath = os.getcwd()
    dataPath = os.path.join(basePath, 'images')
    # print(dataPath) #/Users/wonkyoung/opencv/opencvDojang/images
    # 확장자가 jpg인 파일들만 불러옴 -> return 값은 list
    fileNames = glob(os.path.join(dataPath,'*.jpg'))
    # print(fileNames)
    
    return fileNames

# corners: 좌표(startPt, endPt)
def drawROI(img, corners):
    # 박스를 그릴 레이어를 생성 : cpy
    # copy()를 함으로써 원본 이미지인 img를 보호한다
    # cv2.rectangle()은 원본 이미지에 직접 사각형을 그린다.
    # 만약, copy()를 사용하지 않으면 원본 이미지 img에 직접 사각형이 그려져 원본 이미지가 변경된다.
    # copy()를 해서 원본이미지와 copy()이미지를 가중치를 줘서 겹치게 만든다!!
    cpy = img.copy()
    line_c = (128,128,255)
    lineWidth = 2
    cv2.rectangle(cpy, tuple(corners[0]), tuple(corners[1]), color=line_c, thickness=lineWidth)
    
    # alpha=0.3, beta=0.7, gamma=0
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    return disp

# 마우스 콜백 함수 정의
def onMouse(event, x, y, flags, param):
    global startPt, img, ptList, cpy, txtWrData
    # cpy = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        startPt=(x,y)
        print(startPt)
        # ptList.append([x,y])
    elif event == cv2.EVENT_LBUTTONUP:
        ptList = [startPt,(x,y)]
        txtWrData = str(ptList)
        cpy = drawROI(img, ptList)
        startPt = None
        cv2.imshow('label',cpy)
    elif event == cv2.EVENT_MOUSEMOVE:
        if startPt: 
            ptList=[startPt, (x,y)]
            cpy = drawROI(img, ptList)
            cv2.imshow('label',cpy)
   
   
   
   
   
   
# 마우스가 눌리지 않으면 좌표값은 없음
ptList = []
startPt = None
cpy=[]
txtWrData = None

# 이미지 불러오기
fileNames = getImageList()
img = cv2.imread(fileNames[0])

# txt파일로 저장하기 위해 확장자 떼기
# filename, ext = os.path.splitext(fileNames[0])
# print(filename, ext)

cv2.namedWindow('label')    
cv2.setMouseCallback('label', onMouse, [img])
cv2.imshow('label', img)

while True:
    key = cv2.waitKey()
    if key == 27:
        break
    elif key == ord('s'):
        filename, ext = os.path.splitext(fileNames[0])
        txtFilename = filename + '.txt'
        print("before write txt : {}".format(txtWrData))
        f = open(txtFilename,'w')
        f.write(txtWrData)
        f.close()
        
cv2.destroyAllWindows()