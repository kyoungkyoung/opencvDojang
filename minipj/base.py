import cv2, sys
import numpy as np
import os
from glob import glob
import random

# 디버깅을 위한 코드
def debugChk(result):
    print(result)
    cnt = 0
    debugs = [[], None,'', (), {}, [[],[]]]
    for debug in debugs:
        if result == debug:
            cnt += 1            
        else:
            cnt += 0
    print(cnt)    
    if cnt > 0:
        return print('디버그 코드에 걸림 -> 다시 확인!!')
    else:
        return print('success!!')

 

def getFileList():
    # 현재 디렉토리
    basePath = os.getcwd()
    # 원본 이미지 파일 path
    dataPath = os.path.join(basePath, 'org')
    # print(dataPath) #/Users/wonkyoung/opencv/opencvDojang/minipj/org
    fileList = glob(os.path.join(dataPath, '*.jpg'))
    
    return fileList


def createFolder():
    for classname in classList:
        # 기존에 폴더가 있으면 삭제하고, 새로 생성
        # 폴더안에 파일이 존재하더라도, 파일과 폴더를 모두 삭제
        classPath = os.path.join(dataPath,classname)
        print(classPath)
        # 폴더가 존재한다면
        if os.path.isdir(classPath):
            shutil.rmtree(classPath)
        os.makedirs(classPath,exist_ok=True)


def genFileName(self,procName,value=None):
        if procName==funcNum.resize:
            fileName = self.splitName + '_resize_' + str(value) +'.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.rotate:
            fileName = self.splitName + '_rot_' + str(value) +'.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.hflip:
            fileName = self.splitName + '_hflip.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.vflip:
            fileName = self.splitName + '_vflip.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName             



# input  : 원본 파일명
# output : 새로생성될 파일명
def getFileName(imgName, func):

    if func==2:
        # 경로를 제외한 파일명만 오려낸다 -> keyboard_aa_gg.jpg
        baseName = os.path.basename(imgName)

        # 확장자명만 분리 -> keyboard_aa_gg
        baseNameSplit = os.path.splitext(baseName)[0]
        resizeName = baseNameSplit + '_resize_' + '224' + '.jpg'
        return resizeName
    
    
def resizeImg(fileList, size):
    print(size[1])
    
    img1 = cv2.imread(fileList[0])
    dst1 = cv2.resize(img1, (0,0), fx=size[1], fy=size[1], interpolation=cv2.INTER_LANCZOS4)
    dst2 = cv2.resize(img1, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LANCZOS4)
    
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    
def rotate(self, img=None, multi=True, interAngle=20):
        h, w = img.shape[:2]
        # 튜플로 centerPt를 저장
        centerPt = (w/2, h/2)
        if multi:
            for angle in range(interAngle,360,interAngle):
                # getRotationMatrix2D가 알아서 변환행렬 만들어줌
                aff = cv2.getRotationMatrix2D(centerPt, angle, 1)
                dst = cv2.warpAffine(img, aff, (w, h))
                savefileName = self.genFileName(funcNum.rotate,angle)
                cv2.imwrite(savefileName,dst)
        else:
            aff = cv2.getRotationMatrix2D(centerPt, interAngle, 1)
            dst = cv2.warpAffine(img, aff, (w, h))
            savefileName = self.genFileName(funcNum.rotate,angle)
            cv2.imwrite(savefileName,dst)
            return dst

# crop 함수
# 부분별로 잘라서 일부가 나와도 인식이 잘 되도록 학습하기 위한 이미지 생성
def crop_selectROI(img, imgName):
    img = img
    roi = cv2.selectROI(img)
    if roi != (0,0,0,0):
        croped_img = img[roi[1]: roi[1]+roi[3],
                         roi[0]: roi[0]+roi[2]]
        return croped_img
    
# 랜덤 크롭(편함!)
def random_crop(img, crop_size=(224, 224)):
    h, w = img.shape[:2]  # 이미지의 높이와 너비
    crop_h, crop_w = crop_size

    # 크롭할 이미지의 시작 좌표를 랜덤으로 선택
    if h > crop_h and w > crop_w:
        x = random.randint(0, w - crop_w)
        y = random.randint(0, h - crop_h)

        # 이미지 크롭
        cropped_img = img[y:y+crop_h, x:x+crop_w]
        return cropped_img
    else:
        sys.exit('error')

def make_save_path(imgName, pre_img_str):
    # imgName에서 "_" 앞의 텍스트를 폴더명으로 사용
    folder_name = imgName.split('_')[0]
    # 저장할 디렉터리 경로 생성
    data_pre_path = os.path.join(os.getcwd(), f'0912_exercise/data/{folder_name}')
    # 경로가 없으면 생성
    if not os.path.exists(data_pre_path):
        os.makedirs(data_pre_path)
    # 파일 경로 생성
    makeNewFileName = os.path.join(data_pre_path, f'{imgName}_{pre_img_str}.jpg')
    
    return makeNewFileName

# 이미지 저장 함수
def save_image(img, imgName, pre_img_str):
    # save_path = make_save_path(imgName, pre_img_str) 
    save_path = getFileName(imgName, 2) 
    cv2.imwrite(save_path,img)


def main():
    fileList = getFileList()
    print(fileList)
    img = cv2.imread(fileList[0])
    
    asd = crop_selectROI(img,'asd')
    
    resizeImgList = resizeImg(fileList, (224,0.1))
    
    # cv2.imshow('img', img)

    # cv2.waitKey()
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



