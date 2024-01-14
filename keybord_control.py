import fly
from djitellopy import tello
import pygame
from time import sleep
import cv2

fly.init()

dron = tello.Tello()
dron.connect()
print(dron.get_battery())

dron.streamon()
dron.takeoff()





def get_key_input():
    left_right = 0
    forward_back = 0
    up_down = 0
    yaw = 0
    speed = 50

    for event in pygame.event.get():

        if fly.get_key("LEFT"):
            left_right = -speed
        elif fly.get_key("RIGHT"):
            left_right = speed
        if fly.get_key("UP"):
            up_down = speed
        elif fly.get_key("DOWN"):
            up_down = -speed
        if fly.get_key("w"):
            forward_back = speed
        elif fly.get_key("s"):
            forward_back = -speed
        if fly.get_key("a"):
            yaw = speed
        elif fly.get_key("d"):
            yaw = -speed

        if fly.get_key("q"):
            dron.land()
        elif fly.get_key("e"):
            dron.takeoff()

    return [left_right, up_down, forward_back, yaw]


while True:
    image = dron.get_frame_read().frame
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    vals = get_key_input()
    dron.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

