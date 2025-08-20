import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt)
#split logic
    def split(self):
        #remove inital asteroid, if too, small just end there.
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("too small!")
            return
        #generate random spawn angle
        random_angle = random.uniform(20,50)
        #rotate the velocity vector, can we still access the properties of killed objects? YES we can!
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        #create the new asteroid objects
        new_asteroid1 = Asteroid(self.position.x,self.position.y,new_asteroid_radius)
        #either method works for accessing the x and y coords from Vector2 position property
        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2 = Asteroid(self.position[0],self.position[1],new_asteroid_radius)
        new_asteroid2.velocity = new_velocity2











    