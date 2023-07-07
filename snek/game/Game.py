import pygame
import random
from Snake import Snake
from Box import Box

class Game:
    def __init__(self,  is_sim, has_delta, render):
        
        self.has_delta = has_delta
        self.render = render
        self.is_sim = is_sim
        self.width = 500
        self.height = 450

        self.snake = Snake(pos=(255,220))
        self.food = Box((255, 260), (10, 10))
    
        pygame.init()

        self.gameloop()
        

    def gameloop(self):
        getTicksLastFrame = 0
        screen = None
        if self.render:
            screen = pygame.display.set_mode((self.width, self.height))

        while True:

            deltaTime = 0
            if self.has_delta:
                t = pygame.time.get_ticks()
                deltaTime = (t - getTicksLastFrame) / 1000.0

            if self.is_sim:
                self.simulation_step()
            else: 
                self.game_step(deltaTime)

            if self.render:
                self.render_game(screen)
                pass

            getTicksLastFrame = t



    def game_step(self, delta):
        event_list = pygame.event.get()
        for i in event_list:
            if i.type == pygame.QUIT:
                pygame.quit()
                exit()

            self.snake.move(event_list)
            if self.snake.is_eating(self.food):
                rx = random.randint(0, self.width)
                ry = random.randint(0, self.height)
                
                self.food.x = rx
                self.food.y = ry

        pass

    
    def simulation_Step():
        pass



    def render_game(self, screen):
        screen.fill((0, 0, 0))
        self.snake.draw(screen)
        self.food.draw(screen, (0,255,0))
        pygame.display.flip()
        pass
