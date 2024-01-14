import time

import cv2
import numpy as np
from djitellopy import tello

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
me.takeoff()
me.send_rc_control(0, 0, 18, 0)
time.sleep(2.2)


class FaceTracking:
    def __init__(self, fb_range, pid, p_error, w, h, me):
        self.fb_range = fb_range
        self.pid = pid
        self.p_error = p_error
        self.w = w
        self.h = h
        self.me = me

    fb_range = [6200, 6800]
    pid = [0.4, 0.4, 0]
    p_error = 0
    w, h = 360, 240

    def find_face(img):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(imgGray, 1.2, 8)

        my_faces_list = []
        my_faces_list_area = []

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cx = x + w // 2
            cy = y + h // 2
            area = w * h
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            my_faces_list.append([cx, cy])
            my_faces_list_area.append(area)

        if len(my_faces_list_area) != 0:
            i = my_faces_list_area.index(max(my_faces_list_area))
            return img, [my_faces_list[i], my_faces_list_area[i]]

        else:
            return img, [[0, 0], 0]

    def track_face(me, info, w, pid, p_error):
        area = info[1]
        x, y = info[0]
        error = x - w // 2
        speed = pid[0] * error + pid[1] * (error - p_error)
        speed = int(np.clip(speed, -100, 100))

        fb = 0

        if area > me.fb_range[0] and area < me.fb_range[1]:
            fb = 0

        elif area > me.fb_range[1]:
            fb = -20
        elif area < me.fb_range[0] and area != 0:
            fb = 20

        if x == 0:
            speed = 0
            error - 0

        me.send_rc_control(0, fb, 0, speed)
        return error

    def pokretanje_svih_definicija(self):
        while True:
            img = me.get_frame_read().frame
            img = cv2.resize(img, (self.w, self.h))
            img, info = self.find_face(img)
            p_error = self.track_face(self.me, info, self.w, self.p_error)
            print("Center", info[0], "Area", info[1])
            cv2.imshow("Output", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                me.land()
                break
