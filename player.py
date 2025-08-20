#create spaceship for the player
#import circleshape class as the parent for the new player class
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
import pygame
#we initialise the player class with x and y values only, then define the radius as the imported player radius.
#Finally we call the parent classes constructor within the child class constructor, passing in the x, y and newly defined radius values.
class Player(CircleShape):
    def __init__(self,x,y):
        radius = PLAYER_RADIUS
        super().__init__(x,y,radius)
        #don't need to intitalise other properties as handled by the previous constructor.
        self.rotation = 0
        self.refire_time = 0

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

    #creating method to allow rotation of the player object
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    #paste in update method > checks key output and calls relevant method from player object
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.refire_time == 0:
                self.shoot()
        if self.refire_time > 0:
            #have to reduce by delta time to align with seconds
            self.refire_time -= dt
        if self.refire_time < 0:
            self.refire_time = 0

    #add move method for player object
    def move(self,dt):
        #vector math use a unit vector (one unit going straight up, then rotate the vector by the objects current rotation)
        #then on next line update the position by the player speed (factoring in the delta time dt)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        #create new shot object
        x = self.position[0]
        y = self.position[1]
        bullet = Shot(x,y)

        #set shot velocity
        initalvelocity = pygame.Vector2(0,1)
        rotatedvelocity = initalvelocity.rotate(self.rotation)
        bullet.velocity = rotatedvelocity * PLAYER_SHOT_SPEED
        self.refire_time = PLAYER_SHOOT_COOLDOWN



