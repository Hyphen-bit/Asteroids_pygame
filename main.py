# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
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
    #create groups to manage objects, now refrence groups instead of individual objects when updating
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shotgroup = pygame.sprite.Group()

    Player.containers = (updatables,drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shotgroup,updatables,drawables)
    


    #ensure player object created after setting groups to ensure they are correctly added to the groups

    spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Astrofield = AsteroidField()

    #loop forever unless interupted
    while True:
        #make the close button on the screen display work by checking for a quit event.
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        #display black scren and refresh screen during each loop.
        #UPDATING?____________________________________________________________
        dt = clock.tick(60) / 1000
        updatables.update(dt)
        for asteroid in asteroids:
           if asteroid.collision(spaceship):
              print("Game over!")
              return
        #RENDERING____________________________________________________________
        screen.fill(0)
        #call the draw method of the player object to rerender the player each refresh
        #now iterate over drawables to draw all in group rather than just player object.
        for item in drawables:
           item.draw(screen)

        pygame.display.flip()
        #limit refresh to 1/60th second, and store number of seconds (converted from miliseconds in the DT variable)
        clock.tick(60)



if __name__ == "__main__":
    main()
