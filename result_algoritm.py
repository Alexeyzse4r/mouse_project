import cv2
import sys
import time

import win32con
import time
import win32api
import pyautogui

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

def Scrol(cur):
#    win32api.SetCursorPos((int(height/2), int(width/2)))
    win32api.SetCursorPos((700, 700))
    time.sleep(0.2)
    pyautogui.vscroll(cur)
    time.sleep(0.2)

x_abs, y_abs = 320, 240

tracker_1 = cv2.TrackerKCF_create()
#video = cv2.VideoCapture('video.mp4')
video = cv2.VideoCapture(1)



ok,frame=video.read()
time.sleep(1)
ok,frame=video.read()
height, width, _ = frame.shape

bbox_1 = (0, 0, int(width), int(height))
ok = tracker_1.init(frame,bbox_1)

x, y, w, h, = 0, 0, 0, 0

while True:
   #time.sleep(3)
   ok,frame=video.read()
   if not ok:
        break
   ok,bbox_1=tracker_1.update(frame)
   if ok:
        x_abs, y_abs = int(x+w/2), int(y+h/2)
        (x,y,w,h)=[int(v) for v in bbox_1]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
        #cv2.circle(frame, (int(x+w/2), int(y+h/2)), 5, (255, 0, 0), -1)
        #print('X>>> ', int(x+w/2), '     Y>>> ', int(y+h/2))
        #print(((int(960 - (320 + (x+w/2))*3),' ---------- ', int(540 - (240 - (y+h/2))*3))))
        #x_cur, y_cur = win32api.GetCursorPos()
        print((int(960 + (320 + (x+w/2))*3), int(540 - (240 - (y+h/2))*3)))
        win32api.SetCursorPos((int(540 - (240 - (y+h/2))*5), int(960 - (320 - (x+w/2))*5)))
        #x_abs, y_abs = x_cur, y_cur
   else:
       pass
        #cv2.putText(frame,'Error',(100,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
   cv2.imshow('Tracking',frame)
   if cv2.waitKey(1) & 0XFF==27:
        break
cv2.destroyAllWindows()