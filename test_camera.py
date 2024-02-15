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

rect5X = 765
rect5Y = 312
myRectangle5 = pygame.Rect(rect5X, rect5Y, 40, rectHeight)

rect6X = 765
rect6Y = 444
myRectangle6 = pygame.Rect(rect6X, rect6Y, 40, rectHeight)

rect7X = 695
rect7Y = 379
myRectangle7 = pygame.Rect(rect7X, rect7Y, 40, rectHeight)

rect8X = 835
rect8Y = 377
myRectangle8 = pygame.Rect(rect8X, rect8Y, 40, rectHeight)

joystick_image = pygame.image.load("joystic.png")
joystick_rect = joystick_image.get_rect()

# import fly
# from djitellopy import tello
# import pygame
# from time import sleep
# import face_tracking

# fly.init()
#
# dron = tello.Tello()
# dron.connect()
# print(dron.get_battery())
#
# dron.streamon()
# dron.takeoff()

def main():
    global FPSCLOCK, DISPLAYSURF, event
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((boardWidth, boardHeight))
    pygame.display.set_caption("JOYSTICK")

    mousex = 0
    mousey = 0

    transparent_surface1 = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
    transparent_surface1.fill(BEFORECLICK + (0,))
    transparent_surface2 = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
    transparent_surface2.fill(BEFORECLICK + (0,))
    transparent_surface3 = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
    transparent_surface3.fill(BEFORECLICK + (0,))
    transparent_surface4 = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
    transparent_surface4.fill(BEFORECLICK + (0,))
    transparent_surface5 = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
    transparent_surface5.fill(BEFORECLICK + (0,))
    transparent_surface6 = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
    transparent_surface6.fill(BEFORECLICK + (0,))
    transparent_surface7 = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
    transparent_surface7.fill(BEFORECLICK + (0,))
    transparent_surface8 = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
    transparent_surface8.fill(BEFORECLICK + (0,))

    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(joystick_image, joystick_rect)

        DISPLAYSURF.blit(transparent_surface1, myRectangle1.topleft)
        DISPLAYSURF.blit(transparent_surface2, myRectangle2.topleft)
        DISPLAYSURF.blit(transparent_surface3, myRectangle3.topleft)
        DISPLAYSURF.blit(transparent_surface4, myRectangle4.topleft)
        DISPLAYSURF.blit(transparent_surface5, myRectangle5.topleft)
        DISPLAYSURF.blit(transparent_surface6, myRectangle6.topleft)
        DISPLAYSURF.blit(transparent_surface7, myRectangle7.topleft)
        DISPLAYSURF.blit(transparent_surface8, myRectangle8.topleft)

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
        if mouseClicked and mouseOver1:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle1)

        mouseOver2 = determine_mouseOver(mousex, mousey, myRectangle2)
        if mouseClicked and mouseOver2:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle2)

        mouseOver3 = determine_mouseOver(mousex, mousey, myRectangle3)
        if mouseClicked and mouseOver3:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle3)

        mouseOver4 = determine_mouseOver(mousex, mousey, myRectangle4)
        if mouseClicked and mouseOver4:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle4)

        mouseOver5 = determine_mouseOver(mousex, mousey, myRectangle5)
        if mouseClicked and mouseOver5:
            DISPLAYSURF.blit(transparent_surface5, myRectangle5.topleft)

        mouseOver6 = determine_mouseOver(mousex, mousey, myRectangle6)
        if mouseClicked and mouseOver6:
            DISPLAYSURF.blit(transparent_surface6, myRectangle6.topleft)

        mouseOver7 = determine_mouseOver(mousex, mousey, myRectangle7)
        if mouseClicked and mouseOver7:
            DISPLAYSURF.blit(transparent_surface6, myRectangle7.topleft)

        mouseOver8 = determine_mouseOver(mousex, mousey, myRectangle8)
        if mouseClicked and mouseOver8:
            DISPLAYSURF.blit(transparent_surface6, myRectangle8.topleft)

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
                forward_back = speed

        elif mouseOver4 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle4, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("back")
                forward_back = -speed

        elif mouseOver5 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle5, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("up")
                up_down = -speed

        elif mouseOver6 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle6, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("down")
                up_down = -speed

        elif mouseOver7 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle7, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("left rotate")
                yaw = -speed

        elif mouseOver8 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle8, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("right rotate")
                yaw = speed

        pygame.display.update()
        FPSCLOCK.tick(30)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        # dron.send_rc_control(left_right, 0, up_down, 0)


def determine_mouseOver(valx, valy, rectangle):
    if rectangle.collidepoint(valx, valy):
        return True
    else:
        return False


main()
