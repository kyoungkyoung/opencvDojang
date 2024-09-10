import cv2, sys
import numpy as np
from glob import glob
import os

ptList = []
ptListTxt = ''
img = []
result = []
startPt = None

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
    
    print('ddhsldhlshdlshdls')
    
    startRec = ptList[0]
    lastRec = ptList[1]
    
    cpy = img.copy()
    line_c = (128,128,255)
    lineWidth = 2
    cv2.rectangle(cpy, tuple(startRec), tuple(lastRec), line_c, lineWidth)

    result = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    return result


# 마우스 콜백 함수
def onMouse(event, x, y, flags, param):
    global ptList, ptListTxt, img, result, startPt
    
    # img = param[0]
    if event == cv2.EVENT_LBUTTONDOWN:
        print('마우스 왼쪽버튼 누름')
        startPt = (x,y) # 튜플형식으로 좌표 지정
        print(startPt)
        # ptList.append(startPt)
        
    elif event == cv2.EVENT_LBUTTONUP:
        print('마우스 왼쪽버튼 뗌')
        endPt = (x,y)
        ptList = [startPt, endPt]
        ptListTxt = str(ptList)
        print(ptList)
        result = drawRec(img, ptList)
        startPt = None
        cv2.imshow('img', result)
        ptList = []
        
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스 좌표 x={}, y={}'.format(x,y))
        if startPt:
            print('bbbbbbb')
            endPt = (x,y)
            ptList = [startPt, endPt]
            result = drawRec(img, ptList)
            cv2.imshow('img', result)
    
def main():
    global img
    # 이미지 불러오기
    fileList = getFileList()
    # print(fileList)
    img = cv2.imread(fileList[0])
    
    cv2.namedWindow('img')
    cv2.setMouseCallback('img', onMouse, [img])
    cv2.imshow('img', img)
    
    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()