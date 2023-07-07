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
        print((self.x+self.size/2, self.y-self.size/2, self.size, self.size))


    def move(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x -= 10
                    print("left")
                if event.key == pygame.K_RIGHT:
                    self.x += 10
                    print("right")
                if event.key == pygame.K_UP:
                    self.y -= 10
                    print("down")
                if event.key == pygame.K_DOWN:
                    self.y += 10
                    print("up")



    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 0, 0), pygame.Rect(self.x+self.size/2, self.y-self.size/2, self.size, self.size))
        pass