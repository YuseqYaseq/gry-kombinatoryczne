from time import sleep

import pygame
import sys

from game.game import Game


class App:

    def __init__(self, N, k, d):
        pygame.init()

        # Game stats
        self.set_size = N
        self.k = k
        self.d = d

        self.fps = 60
        self.time_before_restart = 10_000  # 10s
        self.window_width = 1200
        self.window_height = 800
        self.scroll_speed = 2
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        self.game = Game(self.screen, self.set_size, self.k, self.d)

    def run(self):
        self.game.reset(self.set_size, self.k)
        clock = pygame.time.Clock()

        restart_timer = 0
        while True:
            ms_elapsed = clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 5:
                        self.game.scroll_up(ms_elapsed * self.scroll_speed)
                    elif event.button == 4:
                        self.game.scroll_down(ms_elapsed * self.scroll_speed)
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.game.screen = self.screen
                    self.game.set_elements_positions()

            self.game.draw()
            pygame.display.update()
            self.game.update(dt=ms_elapsed)

            if self.game.finished:
                restart_timer += ms_elapsed
            if restart_timer >= self.time_before_restart:
                if self.game.winner == 0:
                    print("Draw!")
                elif self.game.winner == 1:
                    print("Player 1 won!")
                else:
                    print("Player 2 won!")
                break
