import cv2, sys, os, random
import numpy as np
from glob import glob
import shutil

FOLDERLIST = ['keyboard1', 'keyboard2', 'keyboard3']

# 디버깅을 위한 코드
def debugChk(result):
    print(result)
    cnt = 0
    debugs = [[], None, '', (), {}, [[],[]], 'numpy.ndarray']
        
    for debug in debugs:
        if result == debug or type(result) == debug:
            cnt += 1
        else:
            cnt += 0
    print(cnt)    
    if cnt > 0:
        return print('디버그 코드에 걸림 -> 다시 확인!!')
    else:
        return print('success!!')


# 폴더 만들기
def createFolder():
    # print(len(fileList), len(imgList))
    global FOLDERLIST
    for folder in FOLDERLIST:
        currentPath = os.getcwd()
        folderPath = os.path.join(currentPath,folder)
        
        if os.path.isdir(folder):
            shutil.rmtree(folder)
        os.makedirs(folderPath, exist_ok=True)


# 파일 불러오기
def getFileList(originFolder, imgType):
    # 현재 디렉토리
    # /Users/wonkyoung/opencv/opencvDojang/minipj
    basePath = os.getcwd()
    dataPath = os.path.join(basePath,originFolder)
    fileList = glob(os.path.join(dataPath,imgType))
    # debugChk(fileList)
    return fileList


# 이미지 크랍
def cropImg(fileList, ratio):
    cropFileList = []
    
    for i, file in enumerate(fileList):
        i = cv2.imread(file)
        h, w = i.shape[:2]
        centerY = int(h // 2)
        centerX = int(w // 2)

        cropped_img = i[centerY-int(min(h,w)/2):centerY+int(min(h,w)/2),\
            centerX-int(min(h,w)/2):centerX+int(min(h,w)/2)]
        
        cropFileList.append(cropped_img)
        
        # cv2.imshow(f'img{i}', cropped_img)
    return cropFileList
    
    
# 이미지 리사이즈
def resizeImg(fileList, crImgList, imgSize=(224,224)):
    resizeList = []
    cnt=0
    for i in range(len(crImgList)):
        
        i = cv2.resize(crImgList[i], imgSize, fx=imgSize[0], fy=imgSize[1], interpolation=cv2.INTER_LANCZOS4)
    
        resizeList.append(i)
        cnt +=1
    
    return resizeList


def saveFile(rotFileName, dst):
    splitName = os.path.basename(rotFileName)
    split = splitName.split('_')[0]
    rotFileName2 = os.path.splitext(splitName)[0]+'_rotate'+os.path.splitext(splitName)[1]
    print(split)
    
    #위치지정
    cwd = os.getcwd()
    if split == 'keyboard1':
        filePath = os.path.join(cwd, 'keyboard1')
        fullPath = os.path.join(filePath,rotFileName2)
        print(fullPath)
        cv2.imwrite(fullPath, dst)
        
    if split == 'keyboard2':
        filePath = os.path.join(cwd, 'keyboard2')
        fullPath = os.path.join(filePath,rotFileName2)
        cv2.imwrite(fullPath, dst)
        
    if split == 'keyboard3':
        filePath = os.path.join(cwd, 'keyboard3')
        fullPath = os.path.join(filePath,rotFileName2)
        cv2.imwrite(fullPath, dst)
        
    
    
    
def rotateImg(fileList, reImgList, angle):
    createFolder()
    for i in range(len(reImgList)):
        h, w = reImgList[i].shape[:2]
        centerPt = (w/2,h/2)
        
        for ang in range(0, 360, angle):
            aff = cv2.getRotationMatrix2D(centerPt, ang, 1)
            dst = cv2.warpAffine(reImgList[i], aff, (w,h))
            
            # 파일명 저장을 위해 정보추출
            baseFileName = os.path.splitext(fileList[i])[0]
            rotFileName = baseFileName + str(ang) + '.jpg'
            
            saveFile(rotFileName, dst)


def main():
    # 파일불러오기
    fileList = getFileList('org', '*.jpg')
    # 비율이 맞지않는 이미지를 크랍
    crImgList = cropImg(fileList, (1,1))
        # 이미지 리사이즈(원본 파일 이미지 변환)
    reImgList = resizeImg(fileList, crImgList, (224,224))
    # rotate
    rotateImg(fileList, reImgList, 20)
    
    # 추가 데이터 - crop
    # 추가 데이터 - 명도/채도 조절


if __name__ ==  "__main__":
    main()