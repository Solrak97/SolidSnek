import pygame

from Box import Box


class Snake:
    def __init__(self, pos):
        self.x, self.y = pos
        self.speed = 10
        self.size = 10
        self.head_color = None
        self.snake_color = None
        self.snake_body = [Box(pos, (self.size, self.size))]
        self.last_pos = self.snake_body[-1]


    def forward_movements(self, headpos):
        self.last_pos = (self.snake_body[-1].x, self.snake_body[-1].y)
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].x = self.snake_body[i - 1].x
            self.snake_body[i].y = self.snake_body[i - 1].y
        
        self.snake_body[0].x += headpos[0]
        self.snake_body[0].y += headpos[1]
            

    def is_eating(self, food):
        if self.snake_body[0].is_colliding(food):
            self.snake_body.append(Box((self.last_pos), (self.size, self.size)))
            return True
        return False



    def move(self, event_list):
        x = 0
        y = 0
        trigg = False
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= self.speed
                    trigg = True
                if event.key == pygame.K_RIGHT:
                    x += self.speed
                    trigg = True
                if event.key == pygame.K_UP:
                    y -= self.speed
                    trigg = True
                if event.key == pygame.K_DOWN:
                    y += self.speed
                    trigg = True

                if trigg:
                    self.forward_movements((x, y))
    

    def draw(self, screen):
        for i, box in enumerate(self.snake_body):
            if i == 0:
                box.draw(screen, (255, 255, 0))
            else:
                box.draw(screen, (255, 255, 255))
        pass
