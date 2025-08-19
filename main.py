# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import *
from player import Player
#create clock object and dt variable to manage fps and monitor time between screen updates
clock = pygame.time.Clock()
dt = 0

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
    #initalise the player object, specify x and y values
    spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #loop forever unless interupted
    while True:
        #make the close button on the screen display work by checking for a quit event.
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        #display black scren and refresh screen during each loop.
        screen.fill(0)
        #call the draw method of the player object to rerender the player each refresh
        spaceship.draw(screen)

        pygame.display.flip()
        #limit refresh to 1/60th second, and store number of seconds (converted from miliseconds in the DT variable)
        clock.tick(60)
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
