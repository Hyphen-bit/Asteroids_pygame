# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import *

def main():
    #python style guide https://peps.python.org/pep-0008/#imports
    #pygame documentatioh https://www.pygame.org/docs/ref/pygame.html
    #Initalise pygame
    pygame.init()
    #import constants from file
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #loop forever unless interupted
    while True:
        #make the close button on the screen display work by checking for a quit event.
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        #display black scren and refresh screen during each loop.
        screen.fill(0)
        pygame.display.flip()


if __name__ == "__main__":
    main()
