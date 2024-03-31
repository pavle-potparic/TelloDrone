import pygame
import sys
from pygame.locals import *

FPS = 30
BGCOLOR = (3, 115, 46)
BEFORECLICK = (22, 22, 106)
AFTERCLICK = (200, 200, 200)

boardWidth = 1000
boardHeight = 1000

rect1X = 165
rect1Y = 377
rectWidth = 38
rectHeight = 35
myRectangle1 = pygame.Rect(rect1X, rect1Y, rectWidth, rectHeight)

rect2X = 272
rect2Y = 375
myRectangle2 = pygame.Rect(rect2X, rect2Y, rectWidth, rectHeight)

rect3X = 216.5
rect3Y = 322
myRectangle3 = pygame.Rect(rect3X, rect3Y, 40, rectHeight)

rect4X = 216.5
rect4Y = 430
myRectangle4 = pygame.Rect(rect4X, rect4Y, 40, rectHeight)


joystick_image = pygame.image.load("joystic.png")
joystick_rect = joystick_image.get_rect()

import fly
from djitellopy import tello
import pygame
from time import sleep
import face_tracking

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

        if fly.get_key("f"):
            fb_range = [6200, 6800]
            pid = [0.4, 0.4, 0]
            p_error = 0
            w, h = 360, 240
            pokretanje = face_tracking.FaceTracking(fb_range, pid, p_error, w, h, dron)
            pokretanje.pokretanje_svih_definicija()

    return [left_right, up_down, forward_back, yaw]

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((boardWidth, boardHeight))
    pygame.display.set_caption("JOYSTICK")

    mousex = 0
    mousey = 0

    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(joystick_image, joystick_rect)
        pygame.draw.rect(DISPLAYSURF, BEFORECLICK, myRectangle1)
        pygame.draw.rect(DISPLAYSURF, BEFORECLICK, myRectangle2)
        pygame.draw.rect(DISPLAYSURF, BEFORECLICK, myRectangle3)
        pygame.draw.rect(DISPLAYSURF, BEFORECLICK, myRectangle4)
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
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        mouseOver1 = determine_mouseOver(mousex, mousey, myRectangle1)
        if mouseOver1 and mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle1)

        mouseOver2 = determine_mouseOver(mousex, mousey, myRectangle2)
        if mouseOver2 and mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle2)

        mouseOver3 = determine_mouseOver(mousex, mousey, myRectangle3)
        if mouseOver3 and mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle3)

        mouseOver4 = determine_mouseOver(mousex, mousey, myRectangle4)
        if mouseOver4 and mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle4)

        elif mouseOver1 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle1, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("left")
                left_right = -speed

        elif mouseOver2 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle2, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("right")
                left_right = speed

        elif mouseOver3 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle3, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("forward")
                up_down = speed

        elif mouseOver4 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle4, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("back")
                up_down = -speed


        pygame.display.update()
        FPSCLOCK.tick(30)

        dron.send_rc_control(left_right, 0, up_down, 0)

def determine_mouseOver(valx, valy, rectangle):
    if rectangle.collidepoint(valx, valy):
        return True
    else:
        return False

main()
