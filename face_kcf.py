import cv2
import time
import win32api
import dlib
import keyboard
import pyautogui
detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

x_abs, y_abs = 320, 240

video = cv2.VideoCapture(0)

def face_find():
    x1, y1, x2, y2 = 0, 0, 0, 0
    while(1):
        ok, frame = video.read()
        gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        if(faces):
            x1 = faces[0].left()  # left point
            y1 = faces[0].top()  # top point
            x2 = faces[0].right()  # right point
            y2 = faces[0].bottom()  # bottom point
            break

    return (x1 + 30, y1, x2 - x1 - 30, int((y2 - y1) * 0.9))

ok,frame=video.read()
time.sleep(1)
ok,frame=video.read()
height, width, _ = frame.shape

bbox_1 = face_find()
print(bbox_1)
ok,frame=video.read()
number_trak = 0
mass_trak = []

width_disp, height_disp = 1920, 1080
x_last, y_last = width, height

ok, frame = video.read()
for i in range(5):
    tracker_1 = cv2.TrackerCSRT_create()
    tracker_1.retval()
    mass_trak.append(tracker_1)

ok = mass_trak[number_trak].init(frame, bbox_1)
while True:
    # time.sleep(3)
    ok, frame = video.read()
    if not ok:
        break
    ok, bbox_1 = mass_trak[number_trak].update(frame)
    if ok:
        if keyboard.is_pressed('ctrl'):
            pyautogui.click(win32api.GetCursorPos())
        (x, y, w, h) = [int(v) for v in bbox_1]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
        if(abs(x_last - (x + w / 2)) > 2 or abs(y_last - (y + h / 2))>2):
            x_last, y_last = (x + w / 2), (y + h / 2)
            win32api.SetCursorPos((int(width_disp/2 + (width/2 - (x + w / 2)) * 4.5), int(height_disp/2 - (height/2 - (y + h / 2)) * 4.5)))
    else:
        if number_trak>3:
            print('Please, reset this program')
            break
        number_trak+=1
        bbox_1 = face_find()
        ok = mass_trak[number_trak].init(frame, bbox_1)
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break
cv2.destroyAllWindows()

