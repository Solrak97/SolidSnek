import pygame

class Snake:
    def __init__(self, pos):
        self.x, self.y = pos
        self.speed = 10
        self.size = 10
        self.head_color = None
        self.snake_color = None
        self.snake_body = [pos]
        self.last_pos = self.snake_body[-1]


    def move(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1 -= 10
                if event.key == pygame.K_ReventGHT:
                    x1 += 10
                if event.key == pygame.K_UP:
                    y1 -= 10
                if event.key == pygame.K_DOWN:
                    y1 += 10



    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 0, 0), pygame.Rect(30, 30, 60, 60))
        pass