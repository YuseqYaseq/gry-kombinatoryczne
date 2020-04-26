import pygame
import sys

from game.game import Game


class App:

    def __init__(self):
        pygame.init()

        # Game stats
        self.set_size = 50
        self.k = 3

        self.fps = 60
        self.window_width = 1200
        self.window_height = 800
        self.scroll_speed = 2
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        self.game = Game(self.screen, self.set_size, self.k)

    def run(self):
        self.game.reset(self.set_size, self.k)
        clock = pygame.time.Clock()
        while not self.game.finished:
            ms_elapsed = clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.game.scroll_up(ms_elapsed * self.scroll_speed)
                    elif event.button == 5:
                        self.game.scroll_down(ms_elapsed * self.scroll_speed)
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.game.screen = self.screen
                    self.game.set_elements_positions()

            self.game.draw()
            pygame.display.update()
            self.game.update(dt=ms_elapsed)

        if self.game.winner == 0:
            print("Draw!")
        elif self.game.winner == 1:
            print("Player 1 won!")
        else:
            print("Player 2 won!")
