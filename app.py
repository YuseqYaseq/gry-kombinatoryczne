from time import sleep

import pygame
import sys

from game.game import Game


class App:

    def __init__(self, N, k, min_v, max_v, d, bot_wait_time):
        pygame.init()

        self.set_size = N
        self.k = k

        self.fps = 60
        self.window_width = 1200
        self.window_height = 800
        self.scroll_speed = 2
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        self.game = Game(self.screen, N, k, min_v, max_v, d, bot_wait_time)

    def run(self, time_before_restart):
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
            if restart_timer > time_before_restart:
                no_moves = len(self.game.p_nodes[0]) + len(self.game.p_nodes[1])
                return self.game.winner, no_moves
