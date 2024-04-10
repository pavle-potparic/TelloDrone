import cv2
import numpy as np
from djitellopy import tello
import time

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
me.takeoff()
me.send_rc_control(0, 0, 22, 0)
time.sleep(2.2)
w, h = 360, 240
fb_range = [6200, 6800]
pid = [0.4, 0.4, 0]
p_error = 0


def find_face(image):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, 1.2, 8)
    my_face_list_c = []
    my_face_list_area = []

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(image, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        my_face_list_c.append([cx, cy])
        my_face_list_area.append(area)

    if len(my_face_list_area) != 0:
        i = my_face_list_area.index(max(my_face_list_area))
        return image, [my_face_list_c[i], my_face_list_area[i]]

    else:
        return image, [[0, 0], 0]


def track_face(info, w, pid, p_error):
    area = info[1]
    x, y = info[0]
    fb = 0
    error = x - w // 2
    speed = pid[0] * error + pid[1] * (error - p_error)
    speed = int(np.clip(speed, -100, 100))

    if fb_range[0] < area < fb_range[1]:
        fb = 0

    elif area > fb_range[1]:
        fb = -20

    elif area < fb_range[0] and area != 0:
        fb = 20

    if x == 0:
        speed = 0
        error = 0

    me.send_rc_control(0, fb, 0, speed)
    return error


while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = find_face(img)
    p_error = track_face(info, w, pid, p_error)
    cv2.imshow("Output", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break

