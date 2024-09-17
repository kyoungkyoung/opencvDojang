# 1. 배경 : 흰색 책상, 우드 테이블
# 2. 데이터 증식 조건
#    2.0 스마트폰으로 사진 촬영 후 이미지 크기를 줄여주자. (이미지 크기 224x224)
#        대상물 촬영을 어떻게 해야할 지 확인
#    2.1 rotate : 회전(10-30도) 범위 안에서 어느 정도 각도를 넣어야 인식이 잘 되는가?
#    2.2 hflip, vflip : 도움이 되는가? 넣을 것인가? , 과연 이 각도를 넣을 이유가 있을까?
#    2.3 resize, crop : 가능하면 적용해보자
#    2.4 파일명을 다르게 저장 cf) jelly_wood.jpg, lly_white.jpg, jelly_wood_rot_15.jpg
#    2.5 클래스 별로 폴더를 생성
#    2.6 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1-2줄로 요약

# 구성 순서
# 1. 촬영
# 2. 이미지 컴퓨터로 복사, resize
# 3. 육안으로 확인, 이렇게 사용해도 되는가?
# 4. 함수들을 만든다. resize, rotate, hflip, vflip, crop
#    원본파일명을 읽어서 파일명을 생성하는 기능은 모든 함수에 있어야 한다.(함수)
# 5. 단일 함수들 검증
# 6. 함수를 활용해서 기능 구현
# 7. 테스트(경우의 수)
# 8. 데이터셋을 teachable machine사이트에 올려서 테스트
# 9. 인식이 잘 안되는 케이스를 분석하고 케이스 추가 -> 1~8에서 구현된 기능을 이용je


# 어떠한 객체를 생성할 것인가 -> 해당 클래스를 어떻게 구성할 것인가(무엇을 중심으로 클래스를 만들것인가)
# 의 방식으로 구조를 생각
# 클래스를 상속 받을 때 -> 기존 코드에 영향을 주지 않고 버전 추가의 방식으로 구성할 때 -> 기존 코드 수정 X
# 클래스를 추가할 때 -> 




import cv2, sys
import numpy as np
import os
from glob import glob
import shutil
from enum import Enum

# 클래스에 내장될 기능을 번호로 설정
class funcNum(Enum):
    resize = 1
    rotate = 2
    hflip = 3
    vflip = 4
    crop = 5
    
dataPath = os.path.join(os.getcwd(), 'minipj')
dataOrg = os.path.join(dataPath, 'org')

DEBUG = True

# input: dataPath
# output: dataPath 안에 jpg 파일의 리스트를 가져오기
# 확장하려면 기능 추가 -> img_type = ['jpg', 'png', 'gif']
def getFileList(dataPath):
    fileNames = glob(os.path.join(dataPath, '*.jpg'))
    print(fileNames)
    if DEBUG:
        print(fileNames)
        
    return fileNames

# 이미지를 불러오는 함수
def readImg(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        sys.exit('Image load failed')
        
    return img


dsize = (224,224) #전역변수
def resize(img=None, dsize=dsize):
    if img is None:
        print("image Path is None")
        
    dst = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
    
    # 파일명 생성
    # 파일 저장







def main():
    fileNames = getFileList(dataOrg)
    print(len(fileNames))
   
        
if __name__ == "__main__":
    main()