import pygame

class Box:
    def __init__(self, pos, size):
        self.x, self.y = pos
        self.width, self.height = size
        pass


    def is_colliding(self, other):
        return self.x < other.x + other.width and\
        self.x + self.width > other.x and\
        self.y < other.y + other.height and\
        self.y + self.height > other.y
    

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, pygame.Rect(self.x+self.width/2, self.y-self.height/2, self.width, self.height))