import pygame
import sys

# Inicijalizacija Pygame
pygame.init()

# Definisanje dimenzija prozora
win_width = 600
win_height = 400

# Setovanje prozora
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pygame Prozor")

# Boje
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definisanje kvadrata (x, y, width, height)
square = pygame.Rect(100, 100, 100, 100)

# Glavna petlja
while True:
    win.fill(WHITE)
    # Crtanje kvadrata
    pygame.draw.rect(win, BLACK, square)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Proverava da li je klik miša unutar kvadrata
            if square.collidepoint(event.pos):
                print("Kvadrat je kliknut!")

    pygame.display.update()
