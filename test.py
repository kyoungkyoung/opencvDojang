import cv2, sys
import numpy as np
from glob import glob
import os

ptList = []
ptListTxt = ''
img = []
result = []

# 파일 목록 불러오기
def getFileList():
    basePath = os.getcwd()
    # print(basePath) #/Users/wonkyoung/opencv/opencvDojang
    dataPath = os.path.join(basePath, 'images')
    # print(dataPath) #/Users/wonkyoung/opencv/opencvDojang/images
    fileList = glob(os.path.join(dataPath,'*.jpg'))
    # print(fileList) # jpg파일의 절대 경로 출력
    
    return fileList

def drawRec(img, ptList):
    global result
    
    startRec = ptList[0]
    lastRec = ptList[1]
    
    cpy = img.copy()
    line_c = (128,128,255)
    lineWidth = 2
    cv2.rectangle(cpy, tuple(startRec), tuple(lastRec), color=line_c, thickness=lineWidth)

    result = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    return result


# 마우스 콜백 함수
def onMouse(event, x, y, flags, param):
    global ptList, ptListTxt, img, result
    
    # img = param[0]
    startPt = ()
    endPt = ()
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print('마우스 왼쪽버튼 누름')
        startPt = (x,y) # 튜플형식으로 좌표 지정
        ptList.append(startPt)
        # print(ptList)
        
    elif event == cv2.EVENT_LBUTTONUP:
        print('마우스 왼쪽버튼 뗌')
        endPt = (x,y)
        ptList.append(endPt)
        ptListTxt = str(ptList)
        # print(ptList)
        result = drawRec(img, ptList)
        cv2.imshow('img', result)
        ptList = []  # 좌표 초기화
        
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스 좌표 x={}, y={}'.format(x,y))
        if startPt:  # 시작점이 존재하면
            endPt = (x,y)
            ptList[1] = endPt  # 마우스 움직임에 따라 마지막 좌표 업데이트
            result = drawRec(img, ptList)  # 사각형 그리기
            cv2.imshow('img', result)
    
def main():
    global img
    # 이미지 불러오기
    fileList = getFileList()
    # print(fileList)
    img = cv2.imread(fileList[0])
    
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.setMouseCallback('img', onMouse, [img])
    
    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()