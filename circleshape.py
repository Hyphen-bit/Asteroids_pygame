#create circleshape that inherits from the Spirte class within pygame. (pasted code)
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self,CircleShapeObject):
        ##use the built in method distance_to as the position properties of circle shape objects and their children are pygame.Vector2's
        distance = self.position.distance_to(CircleShapeObject.position)
        collision_distance = self.radius + CircleShapeObject.radius
        if distance <= collision_distance:
            return True
        else:
            return False
        