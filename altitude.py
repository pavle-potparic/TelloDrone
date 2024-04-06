import pygame
import sys
from pygame.locals import *
from djitellopy import Tello
import cv2

FPS = 30
BGCOLOR = (3, 115, 46)
BEFORECLICK = (22, 22, 106)
AFTERCLICK = (200, 200, 200)
FONT_COLOR = (255, 255, 255)

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

rect9X = 350
rect9Y = 490
rect9Width = 50
rect9Height = 50
myRectangle9 = pygame.Rect(rect9X, rect9Y, rect9Width, rect9Height)

rect10X = 623
rect10Y = 490
rect10Width = 50
rect10Height = 50
myRectangle10 = pygame.Rect(rect10X, rect10Y, rect10Width, rect10Height)

rectCameraX = 491
rectCameraY = 503
rectCameraWidth = 40
rectCameraHeight = 40
myRectangleCamera = pygame.Rect(rectCameraX, rectCameraY, rectCameraWidth, rectCameraHeight)
cameraOn = False
stepeni = 0

joystick_image = pygame.image.load("joystic.png")
joystick_rect = joystick_image.get_rect()


#
#
# dron = Tello()
# dron.connect()
# print(dron.get_battery())
#
# dron.streamon()

def ability_after_click(click, rect, over_rect):
    if click and over_rect:
        pygame.draw.rect(DISPLAYSURF, AFTERCLICK, rect)


def main():
    global FPSCLOCK, DISPLAYSURF, event, dron, stepeni, cameraOn
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((boardWidth, boardHeight))
    pygame.display.set_caption("JOYSTICK")

    font = pygame.font.Font(None, 36)

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
    transparent_surface9 = pygame.Surface((rect9Width, rect9Height), pygame.SRCALPHA)
    transparent_surface9.fill(BEFORECLICK + (0,))
    transparent_surface10 = pygame.Surface((rect10Width, rect10Height), pygame.SRCALPHA)
    transparent_surface10.fill(BEFORECLICK + (0,))
    transparent_surfaceCamera = pygame.Surface((rectCameraWidth, rectCameraHeight), pygame.SRCALPHA)
    transparent_surfaceCamera.fill(BEFORECLICK + (0,))

    last_update_time = pygame.time.get_ticks()
    first_camera = 0

    while True:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - last_update_time) / 1000.0
        last_update_time = current_time
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
        DISPLAYSURF.blit(transparent_surface9, myRectangle9.topleft)
        DISPLAYSURF.blit(transparent_surface10, myRectangle10.topleft)
        DISPLAYSURF.blit(transparent_surfaceCamera, myRectangleCamera.topleft)

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

        mouseOverCamera = determine_mouseOver(mousex, mousey, myRectangleCamera)
        ability_after_click(mouseClicked, myRectangleCamera, mouseOverCamera)

        mouseOver1 = determine_mouseOver(mousex, mousey, myRectangle1)
        ability_after_click(mouseClicked, myRectangle1, mouseOver1)

        mouseOver2 = determine_mouseOver(mousex, mousey, myRectangle2)
        ability_after_click(mouseClicked, myRectangle2, mouseOver2)

        mouseOver3 = determine_mouseOver(mousex, mousey, myRectangle3)
        ability_after_click(mouseClicked, myRectangle3, mouseOver3)

        mouseOver4 = determine_mouseOver(mousex, mousey, myRectangle4)
        ability_after_click(mouseClicked, myRectangle4, mouseOver4)

        mouseOver5 = determine_mouseOver(mousex, mousey, myRectangle5)
        ability_after_click(mouseClicked, myRectangle5, mouseOver5)

        mouseOver6 = determine_mouseOver(mousex, mousey, myRectangle6)
        ability_after_click(mouseClicked, myRectangle6, mouseOver6)

        mouseOver7 = determine_mouseOver(mousex, mousey, myRectangle7)
        ability_after_click(mouseClicked, myRectangle7, mouseOver7)

        mouseOver8 = determine_mouseOver(mousex, mousey, myRectangle8)
        ability_after_click(mouseClicked, myRectangle8, mouseOver8)

        mouseOver9 = determine_mouseOver(mousex, mousey, myRectangle9)
        ability_after_click(mouseClicked, myRectangle9, mouseOver9)

        mouseOver10 = determine_mouseOver(mousex, mousey, myRectangle10)
        ability_after_click(mouseClicked, myRectangle10, mouseOver10)

        if mouseOver1 and not mouseClicked:
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
                up_down = speed

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

        elif mouseOver9 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle9, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("take off")
                dron.takeoff()

        elif mouseOver10 and not mouseClicked:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle10, 3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("land")
                dron.land()

        elif mouseOverCamera:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangleCamera, 3)

        # if mouseOverCamera and mouseClicked:
        #     first_camera = 1
        #     cameraOn = not cameraOn
        #     print(cameraOn)
        #
        # if cameraOn:
        #     dron.streamon()
        #     frame_read = dron.get_frame_read()
        #     cv2.imshow("Camera View", frame_read.frame)
        #
        # if not cameraOn and first_camera == 1:
        #     dron.streamoff()
        #     cv2.destroyWindow("Camera View")

        if mouseOverCamera and mouseClicked:
            with open('cuvanje_slika.txt', 'r') as num_of_pictures:
                number = int(num_of_pictures.read())
            number += 1
            ret, frame = cv2.VideoCapture(0).read()
            cv2.imshow('Camera', frame)
            cv2.imwrite(f'C:/Users/Administrator/PycharmProjects/tello_dron_slike/tello{number}.jpg', frame)
            with open('cuvanje_slika.txt', 'w') as save_change:
                save_change.write(str(number))

        # current_altitude = dron.get_height()
        # text = font.render(f"Visina: {(current_altitude + 40) / 100} m", True, FONT_COLOR)
        # text_rect = text.get_rect(center=(boardWidth // 2, boardHeight - 650))
        #
        # text_rect2 = text.get_rect(center=(boardWidth // 2, boardHeight - 620))
        #
        # DISPLAYSURF.blit(text, text_rect)
        # DISPLAYSURF.blit(text2, text_rect2)

        pygame.display.update()
        FPSCLOCK.tick(30)
        #
        # dron.send_rc_control(left_right, forward_back, up_down, yaw)


def determine_mouseOver(valx, valy, rectangle):
    if rectangle.collidepoint(valx, valy):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
