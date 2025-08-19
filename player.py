#create spaceship for the player
#import circleshape class as the parent for the new player class
from circleshape import CircleShape
from constants import PLAYER_RADIUS
import pygame
#we initialise the player class with x and y values only, then define the radius as the imported player radius.
#Finally we call the parent classes constructor within the child class constructor, passing in the x, y and newly defined radius values.
class Player(CircleShape):
    def __init__(self,x,y):
        radius = PLAYER_RADIUS
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.rotation = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #creating method to draw the player object, had to import pygame here
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
