import cv2
import sys
import time

#tracker_1 = cv2.legacy.TrackerMedianFlow_create()
#tracker_1 = cv2.TrackerKCF_create()
#tracker_1 = cv2.TrackerCSRT_create()
tracker_1 = cv2.legacy.TrackerMOSSE_create()
#video = cv2.VideoCapture('video.mp4')
#video = cv2.VideoCapture('video_finish_1.avi')
video = cv2.VideoCapture(2)
#video = cv2.VideoCapture('fin.avi')



ok,frame=video.read()
time.sleep(3)
ok,frame=video.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
height, width = frame.shape
print(height, width)
#bbox_1 = (int(width*0.3), 0, int(width*0.3), int(height))
bbox_1 = (0, 0, int(width), int(height))
#frame = cv2.Canny(frame, 30, 50)
#bbox_1 = cv2.selectROI(frame)
#bbox_2 = cv2.selectROI(frame)

ok = tracker_1.init(frame,bbox_1)

while True:
   #time.sleep(1)
   ok,frame=video.read()
   frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   #frame = cv2.Canny(frame, 30, 50)
   ok,bbox_1=tracker_1.update(frame)

   if ok:
        (x,y,w,h)=[int(v) for v in bbox_1]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2,1)
        print((x,y))
        #cv2.circle(frame, (int(x+w/2), int(y+h/2)), 5, (255, 0, 0), -1)
        print('X>>> ', int(x+w/2), '     Y>>> ', int(y+h/2),)
   else:
       pass
        #tracker_1 = cv2.legacy.TrackerMOSSE_create()
        #tracker = cv2.TrackerCSRT_create()
        #bbox_1 = cv2.selectROI(frame)
        #bbox_1 = (int(width*0.3), 0, int(width*0.3), int(height))
        #ok = tracker_1.init(frame, bbox_1)
        #cv2.putText(frame,'Error',(100,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
   cv2.imshow('Tracking',frame)
   if cv2.waitKey(1) & 0XFF==27:
        break
cv2.destroyAllWindows()