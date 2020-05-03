from concurrent import futures
import math
from threading import Lock, Condition, Thread
import pygame

from game.player import Player


class Game:

    def __init__(self, screen, set_size, k):

        # Game stuff
        self.player1 = Player(1, 2, k, 2)
        self.player2 = Player(2, 1, k, 2)
        self.bot_move_wait_time = 1_000  # 1 second between every bot move
        self.executor = futures.ThreadPoolExecutor()
        self.future = None
        self.bot_timer = 0.0
        self.current_player_turn = 1  # 1 or 2
        self.p_nodes = [[], []]
        self.no_colored_nodes = 0

        self.finished = False
        self.winner = 0  # 0 (draw) or 1 or 2
        self.set_size = set_size
        self.k = k

        # Drawing stuff
        self.screen = screen
        self.player_box_width = 200
        self.player_box_height1 = 80
        self.player_box_height2 = 40
        self.player_box_margin = 30
        self.player_box_outline_thickness = 13

        self.node_radius = 50
        self.node_margin = 10
        self.node_outline_thickness = 5

        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.font_color = pygame.Color(0x000000FF)

        self.player1_color = pygame.Color('lightblue')
        self.player2_color = pygame.Color('red')
        self.outline_color = pygame.Color('white')
        self.empty_node_color = pygame.Color('gray')
        self.background_color = pygame.Color(0x808080FF)

        # set by set_elements_positions()
        self.nodes_state = None
        self.nodes_in_line = None
        self.first_line_node_x = None
        self.last_line_node_x = None
        self.first_node_y = None
        self.min_node_y = None
        self.max_node_y = None
        self.width, self.height = None, None
        self.player1_box1_x = None
        self.player1_box1_y = None
        self.player2_box1_x = None
        self.player2_box1_y = None

        self.player1_box2_x = None
        self.player1_box2_y = None
        self.player2_box2_x = None
        self.player2_box2_y = None
        self.set_elements_positions()

    def draw(self):
        self.screen.fill(self.background_color)
        self._draw_rect(self.player1_color,
                        self.player1_box1_x,
                        self.player1_box1_y,
                        self.player_box_width,
                        self.player_box_height1,
                        "Player 1")

        self._draw_rect(self.player1_color,
                        self.player1_box2_x,
                        self.player1_box2_y,
                        self.player_box_width,
                        self.player_box_height2)

        self._draw_rect(self.player2_color,
                        self.player2_box1_x,
                        self.player2_box1_y,
                        self.player_box_width,
                        self.player_box_height1,
                        "Player 2")

        self._draw_rect(self.player2_color,
                        self.player2_box2_x,
                        self.player2_box2_y,
                        self.player_box_width,
                        self.player_box_height2)

        if self.first_line_node_x is None:
            raise RuntimeError("You have to reset the game before calling draw()!")

        x, y = self.first_line_node_x, self.first_node_y
        for i in range(1, self.set_size+1):

            if self.nodes_state[i - 1] == 0:
                node_color = self.empty_node_color
            elif self.nodes_state[i - 1] == 1:
                node_color = self.player1_color
            else:
                node_color = self.player2_color

            self._draw_circle(node_color, x + self.node_radius, y, self.node_radius, str(i))

            if i % self.nodes_in_line == 0:
                y += 2 * self.node_radius + self.node_margin
                if self.set_size - i < self.nodes_in_line:
                    x = self.last_line_node_x
                else:
                    x = self.first_line_node_x
            else:
                x += 2 * self.node_radius + self.node_margin

    def update(self, dt):

        # Bot move
        self.bot_timer += dt
        if self.bot_timer >= self.bot_move_wait_time:
            if self.future is None:
                if self.current_player_turn == 1:
                    self.future = self.executor.submit(self.player1.get_move, self.nodes_state.copy())
                else:
                    self.future = self.executor.submit(self.player2.get_move, self.nodes_state.copy())
            else:
                try:
                    move = self.future.result(0.05)
                except futures._base.TimeoutError:
                    return
                self.future = None
                if self.nodes_state[move] != 0:
                    raise RuntimeError("Illegal move!")
                self.nodes_state[move] = self.current_player_turn
                self.p_nodes[self.current_player_turn - 1].append(move)
                self.p_nodes[self.current_player_turn - 1].sort()

                # Check victory conditions
                self.no_colored_nodes += 1
                ap_len = self._find_longest_ap(self.p_nodes[self.current_player_turn - 1])
                if ap_len > self.k:
                    self.finished = True
                    self.winner = self.current_player_turn
                    return
                if self.no_colored_nodes == self.set_size:
                    self.finished = True
                    self.winner = 0  # Draw

                self.current_player_turn = (self.current_player_turn % 2) + 1
                self.bot_timer -= self.bot_move_wait_time

    def scroll_up(self, amount):
        self.first_node_y -= int(amount)
        if self.first_node_y < self.min_node_y:
            self.first_node_y = self.min_node_y

    def scroll_down(self, amount):
        self.first_node_y += int(amount)
        if self.first_node_y > self.max_node_y:
            self.first_node_y = self.max_node_y

    def reset(self, set_size, k):
        self.finished = False
        self.set_size = set_size
        self.nodes_state = [0 for _ in range(self.set_size)]
        self.k = k
        self._calculate_nodes_positions()

    def _calculate_nodes_positions(self):
        remaining_width = self.player2_box1_x - (self.player1_box1_x + self.player_box_width +
                                                 2 * self.player_box_margin + self.node_margin)
        nodes_in_line = remaining_width // (2 * self.node_radius + self.node_margin)
        if self.set_size < nodes_in_line:
            nodes_in_line = self.set_size
        first_line_margin = remaining_width - (nodes_in_line * (2 * self.node_radius + self.node_margin)) + self.node_margin
        num_last_line_nodes = self.set_size % nodes_in_line
        last_line_margin = remaining_width - (num_last_line_nodes * (2 * self.node_radius + self.node_margin)) + self.node_margin
        self.first_line_node_x = self.player1_box1_x + self.player_box_width + self.player_box_margin + first_line_margin // 2
        self.last_line_node_x = self.player1_box1_x + self.player_box_width + self.player_box_margin + last_line_margin // 2
        self.nodes_in_line = nodes_in_line
        self.first_node_y = self.player1_box1_y
        self.max_node_y = self.first_node_y
        self.min_node_y = min(self.max_node_y + self.height - math.ceil(self.set_size / nodes_in_line) *
                              (self.node_radius * 2 + self.node_margin) - 100,
                              self.max_node_y)

    def set_elements_positions(self):
        self.width, self.height = self.screen.get_size()
        self.player1_box1_x = 20
        self.player1_box1_y = 100
        self.player2_box1_x = self.width - self.player1_box1_x - self.player_box_width
        self.player2_box1_y = self.player1_box1_y

        self.player1_box2_x = self.player1_box1_x
        self.player1_box2_y = self.player1_box1_y + self.player_box_height1 + self.player_box_margin
        self.player2_box2_x = self.player2_box1_x
        self.player2_box2_y = self.player1_box2_y
        self._calculate_nodes_positions()

    def _draw_text(self, text, center_x, center_y):
        text = self.font.render(text, True, self.font_color)
        text_rect = text.get_rect(center=(center_x, center_y))
        self.screen.blit(text, text_rect)

    def _draw_rect(self, player_color, x, y, w, h, text=None):
        pygame.draw.rect(self.screen,
                         self.outline_color,
                         pygame.Rect((x, y), (w, h)),
                         self.player_box_outline_thickness)

        pygame.draw.rect(self.screen,
                         player_color,
                         pygame.Rect((x, y), (w, h)))

        if text is not None:
            self._draw_text(text, x + w//2, y+h//2)

    def _draw_circle(self, color, x, y, r, text=None):

        pygame.draw.circle(self.screen,
                           color,
                           (x, y),
                           r)

        pygame.draw.circle(self.screen,
                           self.outline_color,
                           (x, y),
                           r,
                           self.node_outline_thickness)

        if text is not None:
            self._draw_text(text, x, y)

    @staticmethod
    def _find_longest_ap(element_list):

        n = len(element_list)
        if n <= 2:
            return n

        li = [[0 for _ in range(n)] for _ in range(n)]
        llap = 2
        for i in range(n):
            li[i][n - 1] = 2

        for j in range(n - 2, 0, -1):
            i = j - 1
            k = j + 1
            while i >= 0 and k <= n - 1:

                if element_list[i] + element_list[k] < 2 * element_list[j]:
                    k += 1
                elif element_list[i] + element_list[k] > 2 * element_list[j]:
                    li[i][j] = 2
                    i -= 1
                else:
                    li[i][j] = li[j][k] + 1
                    llap = max(llap, li[i][j])
                    i -= 1
                    k += 1
                    while i >= 0:
                        li[i][j] = 2
                        i -= 1
        return llap
