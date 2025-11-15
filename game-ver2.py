import pygame
from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("2-cars")


# load & resize images 
red_car = pygame.image.load('images/red_car.png')
blue_car = pygame.image.load('images/blue_car.png')
w = red_car.get_width() 
h = red_car.get_height()
left_car = pygame.transform.scale(red_car, (w * 0.07, h * 0.07))
right_car = pygame.transform.scale(blue_car, (w * 0.07, h * 0.07))
print(f'left_car: w:{left_car.get_width()} h:{left_car.get_height()}')
print(f'right_car: w:{right_car.get_width()} h:{right_car.get_height()}')

# Set the frame rate
clock = pygame.time.Clock()

pos = {
    'red_left': (22, 650),
    'red_right': (122, 650),
    'blue_left': (222, 650),
    'blue_right': (322, 650),
}
red_left_pos = ()
red_right_pos = ()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (black in this case)
    screen.fill((20, 20, 60))

    # split screen in half
    pygame.draw.line(screen, (50, 50, 100), (200, 0), (200, 800), 3)

    # split lines in each side
    pygame.draw.line(screen, (50, 50, 100), (100, 0), (100, 800), 2)
    pygame.draw.line(screen, (50, 50, 100), (300, 0), (300, 800), 2)


    screen.blit(left_car, pos['red_left'])
    screen.blit(right_car, pos['blue_right'])

    pygame.display.update()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)