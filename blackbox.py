# 블랙박스 만들기
# 1. 60초동안 저장, 동영상 한개가 생성되도록한다.
#    파일명은 20240902-161903.avi
# 2. 폴더 생성은 날짜 + 현재시간
#    20240902-16 00분~59분
#    한시간마다 폴더 생성
# 3. 블랙박스 녹화 폴더가 3GB이면
#    가장 오래된 녹화 폴더 삭제

import os

# 폴더 만들기
# os.mkdir()

# 폴더 용량 읽기
def readDir():
    diskLabel = '/Users/wonkyoung/opencv/opencvDojang'
    print(os.path.getsize(diskLabel))

