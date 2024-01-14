from djitellopy import tello
import pygame

dron = tello.Tello()

dron.connect()
print(dron.get_battery())
dron.takeoff()
def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def get_key(key):
    ans = False

    for event in pygame.event.get():
        pygame.K_LEFT
        pass

    key_input = pygame.key.get_pressed()

    my_key = getattr(pygame, "K_{}".format(key))
    if key_input[my_key]:
        ans = True

    pygame.display.update()
    return ans

def pressedButton():
    return pygame.key.get_pressed();

def main():
    if get_key("LEFT"):
         pass
    if get_key("RIGHT"):
        pass

if __name__ == "main":
    init()
    while True:
        main()



