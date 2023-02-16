import cv2
import os
from configparser import ConfigParser

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, '../config/config.ini')
config = ConfigParser()
config.read(initfile)

PHOTOS_PATH = config.get('default', 'PHOTOS_PATH')
RTSP_URL = config.get('default', 'RTSP_URL')
RTSP_URL_PORTON = config.get('default', 'RTSP_URL_PORTON')

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

class ColliCameras:

    def takePhoto(self):
        cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

        if not cap.isOpened():
            print('Cannot open RTSP stream')
            exit(-1)

        while True:
            _, frame = cap.read()
            if not _:
                print('failed to grab frame')
                break
            else:
                print('Taking photo, wait ... ')
                cv2.imwrite(PHOTOS_PATH +'patio.png',frame)
                break

        cap.release()

    def takePhoto2(self):
        msg = ""
        status = ""
        cap = cv2.VideoCapture(RTSP_URL_PORTON, cv2.CAP_FFMPEG)

        if not cap.isOpened():
            print('Cannot open RTSP stream')
            status = False
            exit(-1)

        while True:
            _, frame = cap.read()
            if not _:
                msg = "failed to grab frame"
                status = False
                print(msg)
                break
            else:
                print('Taking photo, wait ... ')
                cv2.imwrite(PHOTOS_PATH +'porton.png',frame)
                msg = "Photo taken successfully"
                status = True
                print(msg)
                break

        cap.release()
        
        return {
            "msg" : msg,
            "status" : status
        }

    def cameraPhoto(self,name):
        if name == "patio":
            print("Camara Patio")
            cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
            msg = "Patio done"
        elif name == "porton":
            print("Camara Porton")
            cap = cv2.VideoCapture(RTSP_URL_PORTON, cv2.CAP_FFMPEG)
            msg = "Porton Done"
        else: 
            msg = "Camera not found"

            if not cap.isOpened():
                print('Cannot open RTSP stream')
                exit(-1)

            while True:
                _, frame = cap.read()
                if not _:
                    print('failed to grab frame')
                    break
                else:
                    print('Taking photo, wait ... ')
                    cv2.imwrite(PHOTOS_PATH +'c1.png',frame)
                    break

            cap.release()