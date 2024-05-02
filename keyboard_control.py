import numpy as np
import pygame
import sys
from pygame.locals import *
from djitellopy import Tello
import cv2
import os

CONNECT_DRON = False
FPS = 30
BG_COLOR = (3, 115, 46)
BEFORE_CLICK = (22, 22, 106)
AFTER_CLICK = (200, 200, 200)
FONT_COLOR = (255, 255, 255)

BOARD_WIDTH = 1000
BOARD_HEIGHT = 1000

BUTTON_LEFT_RIGHT_WIDTH = 38

BUTTON_FLY_WIDTH = 50
BUTTON_FLY_HEIGHT = 50

BUTTON_WIDTH_GENERAL = 40
BUTTON_HEIGHT_GENERAL = 35

# params: x, y, width, height
buttonLeft = pygame.Rect(165, 377, BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL)

buttonRight = pygame.Rect(272, 375, BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL)

buttonBack = pygame.Rect(216.5, 322, BUTTON_WIDTH_GENERAL, BUTTON_HEIGHT_GENERAL)

buttonForward = pygame.Rect(216.5, 430, BUTTON_WIDTH_GENERAL, BUTTON_HEIGHT_GENERAL)

buttonUp = pygame.Rect(765, 312, BUTTON_WIDTH_GENERAL, BUTTON_HEIGHT_GENERAL)

buttonDown = pygame.Rect(765, 444, BUTTON_WIDTH_GENERAL, BUTTON_HEIGHT_GENERAL)

buttonLeftRotate = pygame.Rect(695, 379, BUTTON_WIDTH_GENERAL, BUTTON_HEIGHT_GENERAL)

buttonRightRotate = pygame.Rect(835, 377, BUTTON_WIDTH_GENERAL, BUTTON_HEIGHT_GENERAL)

buttonTakeOff = pygame.Rect(350, 490, BUTTON_FLY_WIDTH, BUTTON_FLY_HEIGHT)

buttonLand = pygame.Rect(623, 490, BUTTON_FLY_WIDTH, BUTTON_FLY_HEIGHT)

rectCameraHeight = 40
buttonCamera = pygame.Rect(491, 503, BUTTON_WIDTH_GENERAL, rectCameraHeight)
cameraOn = False

BUTTON_FACE_TRACKING_WIDTH = 25
BUTTON_FACE_TRACKING_HEIGHT = 40
buttonFaceTracking = pygame.Rect(327, 293, BUTTON_FACE_TRACKING_WIDTH, BUTTON_FACE_TRACKING_HEIGHT)

BUTTON_RECORD_WIDTH = 25
BUTTON_RECORD_HEIGHT = 40
buttonRecord = pygame.Rect(669, 293, BUTTON_RECORD_WIDTH, BUTTON_RECORD_HEIGHT)

degree = 0

joystick_image = pygame.image.load("joystic.png")
joystick_rect = joystick_image.get_rect()

if CONNECT_DRON:
    dron = Tello()
    dron.connect()
    print(dron.get_battery())

    dron.streamon()


def change_button_color_after_click(click, rect, over_rect):
    if click and over_rect:
        pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, rect)


def main():
    global FPSCLOCK, DISPLAYSURF, event, dron, degree, cameraOn
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    pygame.display.set_caption("JOYSTICK")

    transparent_surface_button_left = pygame.Surface((BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL), pygame.SRCALPHA)
    transparent_surface_button_left.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_right = pygame.Surface((BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL), pygame.SRCALPHA)
    transparent_surface_button_right.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_back = pygame.Surface((BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL), pygame.SRCALPHA)
    transparent_surface_button_back.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_forward = pygame.Surface((BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL),
                                                        pygame.SRCALPHA)
    transparent_surface_button_forward.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_up = pygame.Surface((BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL), pygame.SRCALPHA)
    transparent_surface_button_up.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_down = pygame.Surface((BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL), pygame.SRCALPHA)
    transparent_surface_button_down.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_left_rotate = pygame.Surface((BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL),
                                                            pygame.SRCALPHA)
    transparent_surface_button_left_rotate.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_right_rotate = pygame.Surface((BUTTON_LEFT_RIGHT_WIDTH, BUTTON_HEIGHT_GENERAL),
                                                             pygame.SRCALPHA)
    transparent_surface_button_right_rotate.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_take_off = pygame.Surface((BUTTON_FLY_WIDTH, BUTTON_FLY_HEIGHT), pygame.SRCALPHA)
    transparent_surface_button_take_off.fill(BEFORE_CLICK + (0,))
    transparent_surface_button_land = pygame.Surface((BUTTON_FLY_WIDTH, BUTTON_FLY_HEIGHT), pygame.SRCALPHA)
    transparent_surface_button_land.fill(BEFORE_CLICK + (0,))
    transparent_surface_camera = pygame.Surface((BUTTON_WIDTH_GENERAL, rectCameraHeight), pygame.SRCALPHA)
    transparent_surface_camera.fill(BEFORE_CLICK + (0,))
    transparent_surface_face_tracking = pygame.Surface((BUTTON_FACE_TRACKING_WIDTH, BUTTON_FACE_TRACKING_HEIGHT),
                                                       pygame.SRCALPHA)
    transparent_surface_face_tracking.fill(BEFORE_CLICK + (0,))
    transparent_surface_record = pygame.Surface((BUTTON_RECORD_WIDTH, BUTTON_RECORD_HEIGHT),
                                                pygame.SRCALPHA)
    transparent_surface_record.fill(BEFORE_CLICK + (0,))

    last_update_time = pygame.time.get_ticks()
    font = pygame.font.Font(None, 36)
    first_camera = 0

    mouse_x = 0
    mouse_y = 0

    while True:
        current_time = pygame.time.get_ticks()
        last_update_time = current_time
        mouse_clicked = False
        DISPLAYSURF.fill(BG_COLOR)
        DISPLAYSURF.blit(joystick_image, joystick_rect)

        DISPLAYSURF.blit(transparent_surface_button_left, buttonLeft.topleft)
        DISPLAYSURF.blit(transparent_surface_button_right, buttonRight.topleft)
        DISPLAYSURF.blit(transparent_surface_button_back, buttonBack.topleft)
        DISPLAYSURF.blit(transparent_surface_button_forward, buttonForward.topleft)
        DISPLAYSURF.blit(transparent_surface_button_up, buttonUp.topleft)
        DISPLAYSURF.blit(transparent_surface_button_down, buttonDown.topleft)
        DISPLAYSURF.blit(transparent_surface_button_left_rotate, buttonLeftRotate.topleft)
        DISPLAYSURF.blit(transparent_surface_button_right_rotate, buttonRightRotate.topleft)
        DISPLAYSURF.blit(transparent_surface_button_take_off, buttonTakeOff.topleft)
        DISPLAYSURF.blit(transparent_surface_button_land, buttonLand.topleft)
        DISPLAYSURF.blit(transparent_surface_camera, buttonCamera.topleft)
        DISPLAYSURF.blit(transparent_surface_face_tracking, buttonFaceTracking.topleft)
        DISPLAYSURF.blit(transparent_surface_record, buttonRecord.topleft)

        left_right = 0
        forward_back = 0
        up_down = 0
        yaw = 0
        speed = 50

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                mouse_clicked = True

        mouseover_camera = determine_mouseover(mouse_x, mouse_y, buttonCamera)
        change_button_color_after_click(mouse_clicked, buttonCamera, mouseover_camera)

        mouseover_button_left = determine_mouseover(mouse_x, mouse_y, buttonLeft)
        change_button_color_after_click(mouse_clicked, buttonLeft, mouseover_button_left)

        mouseover_button_right = determine_mouseover(mouse_x, mouse_y, buttonRight)
        change_button_color_after_click(mouse_clicked, buttonRight, mouseover_button_right)

        mouseover_button_back = determine_mouseover(mouse_x, mouse_y, buttonBack)
        change_button_color_after_click(mouse_clicked, buttonBack, mouseover_button_back)

        mouseover_button_forward = determine_mouseover(mouse_x, mouse_y, buttonForward)
        change_button_color_after_click(mouse_clicked, buttonForward, mouseover_button_forward)

        mouseover_button_up = determine_mouseover(mouse_x, mouse_y, buttonUp)
        change_button_color_after_click(mouse_clicked, buttonUp, mouseover_button_up)

        mouseover_button_down = determine_mouseover(mouse_x, mouse_y, buttonDown)
        change_button_color_after_click(mouse_clicked, buttonDown, mouseover_button_down)

        mouseover_button_left_rotate = determine_mouseover(mouse_x, mouse_y, buttonLeftRotate)
        change_button_color_after_click(mouse_clicked, buttonLeftRotate, mouseover_button_left_rotate)

        mouseover_button_right_rotate = determine_mouseover(mouse_x, mouse_y, buttonRightRotate)
        change_button_color_after_click(mouse_clicked, buttonRightRotate, mouseover_button_right_rotate)

        mouseover_button_take_off = determine_mouseover(mouse_x, mouse_y, buttonTakeOff)
        change_button_color_after_click(mouse_clicked, buttonTakeOff, mouseover_button_take_off)

        mouseover_button_land = determine_mouseover(mouse_x, mouse_y, buttonLand)
        change_button_color_after_click(mouse_clicked, buttonLand, mouseover_button_land)

        mouseover_face_tracking = determine_mouseover(mouse_x, mouse_y, buttonFaceTracking)
        change_button_color_after_click(mouse_clicked, buttonFaceTracking, mouseover_face_tracking)

        mouseover_record = determine_mouseover(mouse_x, mouse_y, buttonRecord)
        change_button_color_after_click(mouse_clicked, buttonRecord, mouseover_record)

        if mouseover_button_left and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonLeft, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("left")
                left_right = -speed

        elif mouseover_button_right and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonRight, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("right")
                left_right = speed

        elif mouseover_button_back and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonBack, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("forward")
                forward_back = speed

        elif mouseover_button_forward and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonForward, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("back")
                forward_back = -speed

        elif mouseover_button_up and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonUp, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("up")
                up_down = speed

        elif mouseover_button_down and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonDown, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("down")
                up_down = -speed

        elif mouseover_button_left_rotate and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonLeftRotate, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("left rotate")
                yaw = -speed

        elif mouseover_button_right_rotate and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonRightRotate, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("right rotate")
                yaw = speed

        elif mouseover_button_take_off and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonTakeOff, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("take off")
                dron.takeoff()

        elif mouseover_button_land and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonLand, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("land")
                dron.land()

        elif mouseover_face_tracking and not mouse_clicked:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonFaceTracking, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('face tracking')
                return False

        elif mouseover_camera:
            pygame.draw.rect(DISPLAYSURF, AFTER_CLICK, buttonCamera, 3)

        if CONNECT_DRON:
            if mouseover_camera and mouse_clicked:
                first_camera = 1
                cameraOn = not cameraOn
                print(cameraOn)

            if cameraOn:
                dron.streamon()
                frame_read = dron.get_frame_read()
                cv2.imshow("Camera View", frame_read.frame)

            if not cameraOn and first_camera == 1:
                dron.streamoff()
                cv2.destroyWindow("Camera View")

        if mouseover_camera and mouse_clicked:
            with open('save_images.txt', 'r') as num_of_pictures:
                number = int(num_of_pictures.read())
            number += 1
            ret, frame = cv2.VideoCapture(0).read()
            cv2.imshow('Camera', frame)
            cv2.imwrite(f'tello_dron_images/tello{number}.jpg', frame)
            with open('save_images.txt', 'w') as save_change:
                save_change.write(str(number))

        if mouseover_record and mouse_clicked:
            putanja_za_cuvanje = 'C:/Users/Administrator/PycharmProjects/tello_dron_slike'
            output_filename = putanja_za_cuvanje + 'output.mp4'

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

            cap = cv2.VideoCapture(0)

            while True:
                ret, frame = cap.read()

                out.write(frame)

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) == ord('q'):
                    break

            cap.release()
            out.release()
            cv2.destroyAllWindows()

            os.startfile(output_filename)

        if CONNECT_DRON:
            current_altitude = dron.get_height()
            text = font.render(f"Visina: {(current_altitude + 40) / 100} m", True, FONT_COLOR)
            text_rect = text.get_rect(center=(BOARD_WIDTH // 2, BOARD_HEIGHT - 650))

            DISPLAYSURF.blit(text, text_rect)

        pygame.display.update()
        FPSCLOCK.tick(30)

        if CONNECT_DRON:
            dron.send_rc_control(left_right, forward_back, up_down, yaw)


def determine_mouseover(valx, valy, rectangle):
    if rectangle.collidepoint(valx, valy):
        return True
    else:
        return False


loop = True
while loop:
    loop = main()


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

    dron.send_rc_control(0, fb, 0, speed)
    return error


if CONNECT_DRON:
    w, h = 360, 240
    fb_range = [6200, 6800]
    pid = [0.4, 0.4, 0]
    p_error = 0
    while True:
        img = dron.get_frame_read().frame
        img = cv2.resize(img, (w, h))
        img, info = find_face(img)
        p_error = track_face(info, w, pid, p_error)
        cv2.imshow("Output", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            dron.land()
            break
