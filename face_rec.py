import cv2
import numpy as np
import dlib
import win32api

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# read the image
video = cv2.VideoCapture(0)

left, right, up, down = 160, -160, 40, 100
# Convert image into grayscale
width_disp, height_disp = 1920, 1080
while(1):

    ok,frame=video.read()
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
    # Use detector to find landmarks
    faces = detector(gray)
    for face in faces:
        x1 = face.left() # left point
        y1 = face.top() # top point
        x2 = face.right() # right point
        y2 = face.bottom() # bottom point

        # Create landmark object
        landmarks = predictor(image=gray, box=face)

        # Loop through all the points
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y

            # Draw a circle
            if n == 27 or n == 0 or n == 16 or n == 8 or n == 30:
                cv2.circle(img=frame, center=(x, y), radius=5, color=(255, 0, 0), thickness=-1)
            else:
                cv2.circle(img=frame, center=(x, y), radius=1, color=(0, 1*n*3, 0), thickness=-1)

        #print('LEFT>>', landmarks.part(0).x, ' --- ', landmarks.part(0).y)
        #print('UP>>', landmarks.part(27).x, ' --- ', landmarks.part(27).y)
        #print('DOWN>>', landmarks.part(8).x, ' --- ', landmarks.part(8).y)
        #print('RIGHT>>', landmarks.part(16).x, ' --- ', landmarks.part(16).y)
        #print('CENTER>>', landmarks.part(30).x, ' --- ', landmarks.part(30).y)

#        if (input() == '1'):
#            left = (landmarks.part(27).x - landmarks.part(0).x) - (landmarks.part(16).x - landmarks.part(27).x)
#            down = (landmarks.part(8).y - landmarks.part(30).y) - (landmarks.part(30).y - landmarks.part(27).y)
#        elif(input() == '2'):
#            right = (landmarks.part(27).x - landmarks.part(0).x) - (landmarks.part(16).x - landmarks.part(27).x)
#            up = (landmarks.part(8).y - landmarks.part(30).y) - (landmarks.part(30).y - landmarks.part(27).y)

        #print('STORONA>> ', (landmarks.part(27).x - landmarks.part(0).x) - (landmarks.part(16).x - landmarks.part(27).x))
        storona = (landmarks.part(27).x - landmarks.part(0).x) - (landmarks.part(16).x - landmarks.part(27).x)
        #print('UP>> ', (landmarks.part(8).y - landmarks.part(30).y) - (landmarks.part(30).y - landmarks.part(27).y))
        tangaj = (landmarks.part(8).y - landmarks.part(30).y) - (landmarks.part(30).y - landmarks.part(27).y)

        #x_cur, y_cur = win32api.GetCursorPos()
        #print((int(960 - (right-left-storona)), int(540 - (up - down-tangaj))))
        #win32api.SetCursorPos((int(width_disp / 2 + (width / 2 - (x + w / 2)) * 4.5), int(height_disp / 2 - (height / 2 - (y + h / 2)) * 4.5)))
        win32api.SetCursorPos((int(width_disp/2 + (right-left-storona)*1.3), int(height_disp/2 + (up - down-tangaj)*1.3)))
    # show the image
    cv2.imshow(winname="Face", mat=frame)

    if cv2.waitKey(1) & 0XFF == 27:
        break

    # Close all windows
cv2.destroyAllWindows()