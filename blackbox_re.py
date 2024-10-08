# 블랙박스 만들기
# 1. 60초동안 저장, 동영상 한개가 생성되도록한다.
#    파일명은 20240902-161903.avi
# 2. 폴더 생성은 날짜 + 현재시간
#    20240902-16 00분~59분
#    한시간마다 폴더 생성
# 3. 블랙박스 녹화 폴더가 3GB이면
#    가장 오래된 녹화 폴더 삭제

'''
1. 60초에 동영상 한 개가 생성되도록 한다.
   파일명은 20240902_161903.avi

2. 폴더 생성은 날짜+현재 시간
   20240902_16 00분~59분
   한 시간마다 폴더 생성

3. 블랙박스 녹화 폴더가 500MB이면
   가장 오래된 녹화 폴더 삭제
'''

import cv2, sys
import os
import threading
import time
from datetime import datetime

recording = True
recording_h = True
rec_len = 5
rec_len_h = 3600

# threading.Event() : 이벤트의 발생 여부를 나타내는 플래그
# 스레드 이벤트 발생여부 감시하는 애
stop_recording = threading.Event()
stop_recording_h = threading.Event()

# 60초 타이머 스레드
def timerThreadSec(stop_event, rec_time):
    global recording
    loop = rec_time
    
# 한번만 하는거라서 계속해서 작동이 되게 해야함. -> while문 밖에 한번더 while문을 건다던지 -> 스레드를 시작하는 함수를 mkVedio()안에 넣어주기
    
    while(recording):
        time.sleep(1)
        loop -= 1
        if loop == 0:
            break
    
    # while문 다 돌면 60초 -> 녹화 중지
    # set() : 이벤트 플래그를 True로 설정하는 역할
    # 스레드의 stop_event를 발생시키는 애 -> 스레드 정지 시키는 애
    stop_event.set()


def timerThreadHour(stop_event_h, rec_time):
    global recording_h
    loop = rec_time
    
    while(recording_h):
        time.sleep(3600)
        loop -= 1
        if loop == 0:
            break
    
    # while문 다 돌면 3600초(1시간) -> 녹화 중지
    # set() : 이벤트 플래그를 True로 설정하는 역할
    # 스레드 stop_event를 발생시키는 애
    stop_event_h.set()


def threadStart():
        
    # 스레드 생성
    timerSec = threading.Thread(target=timerThreadSec, args=(stop_recording, rec_len))
    timerHour = threading.Thread(target=timerThreadHour, args=(stop_recording_h, rec_len_h))
    # timer.start()

# 동영상 생성
def mkVideo(path):
    global recording
    global stop_recording
    global timerSec
    
    cap = cv2.VideoCapture(0)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FRAME_COUNT, 30)
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),\
                 int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    # print(frameSize)
    # print(fps)
    
    # 동영상 파일명 : 20240902_161903.avi
    now = datetime.now()
    fileName = now.strftime("%Y%m%d_%H:%M:%S")
    fileName = fileName + ".mp4"
    folderName = os.path.join(path + '/'+ now.strftime("%Y%m%d_%H"))
    # filePath = os.path.join(folderName,fileName)
    filePath = path+fileName
    out = cv2.VideoWriter(filePath, fourcc, fps, frameSize)
    
    # 60초 스레드 시작
    timerSec.start()
    
    while(recording):
        retval, frame = cap.read()
        
        if retval:
            out.write(frame)
            cv2.imshow('Blackbox', frame)
            
            # 강제 종료
            if cv2.waitKey(1) & 0xFF == 27:
                recording = False
                break
            
        # 타이머 확인 -> 만약 타이머가 멈췄으면 recording=False
        if stop_recording.is_set():
            recording = False
            break
            
    
    cap.release()
    out.release()
    
    cv2.destroyAllWindows()


# 폴더 만들기 - 1시간마다 폴더 생성
def mkFolder(path):
    global recording_h
    global stop_recording_h
    global timerHour
    
    basePath = path
    os.makedirs(basePath, exist_ok=True)
    
    # 스레드 시작 - 1시간
    timerHour.start()
    
    # 폴더 생성
    now = datetime.now()
    folderName = now.strftime("%Y%m%d_")
    folderName = folderName + now.strftime("%H")
    folderName = os.path.join(basePath, folderName)
    os.makedirs(folderName, exist_ok=True)

    # 타이머 확인
    if stop_recording_h.is_set():
        recording_h = False
        
    # for hour in range(24):
    #     folderName = now.strftime("%Y%m%d_")
    #     folderName = folderName + str(hour)
    #     folderName = os.path.join(basePath, folderName)
    #     # print(folderName)
    #     os.makedirs(folderName, exist_ok=True)
    
    return folderName

# 폴더 용량 읽기
def readDir():
    diskLabel = '/Users/wonkyoung/opencv/opencvDojang'
    print(os.path.getsize(diskLabel))



folderName = mkFolder('/Users/wonkyoung/opencv/opencvDojang/test')
mkVideo(f"/Users/wonkyoung/opencv/opencvDojang/test/{folderName}")









# 폴더 용량을 읽을 때 / 디스크 공간을 확인할 때 컴퓨터가 약 1-2초 정도 멈출 수 밖에 없다
# 그럼 그 디스크를 읽는 스레드를 따로 또 만들어서 빼주면 폴더를 만들기 위해 1시간을 카운트하는 스레드를 만들어서 따로 뺀다.
