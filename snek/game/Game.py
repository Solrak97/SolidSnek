import pygame

from Snake import Snake
from Box import Box

class Game:
    def __init__(self,  is_sim, has_delta, render):
        
        self.has_delta = has_delta
        self.render = render
        self.is_sim = is_sim

        self.snake = Snake(pos=(0,0))
        self.food = None
    
        pygame.init()

        self.gameloop()
        

    def gameloop(self):
        getTicksLastFrame = 0
        screen = None
        if self.render:
            screen = pygame.display.set_mode((500, 450))

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

            getTicksLastFrame = t



    def game_step(self, delta):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                exit()

            self.snake.move(pygame.event.get())
        pass

    
    def simulation_Step():
        pass



    def render_game(self, screen):
        screen.fill((255, 255, 255))
        self.snake.render(screen)
        pygame.display.flip
        pass
