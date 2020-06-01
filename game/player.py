from random import randint
from typing import List
from game.alfa_beta import AlfaBeta

class Player:

    def __init__(self, player, enemy, k, max_deepth):
        self.player = player
        self.enemy = enemy
        self.k = k
        self.max_deepth = max_deepth
        
    def get_move(self, nodes: List, values: List):

        alfa_beta = AlfaBeta(values, nodes, self.k, self.player, self.enemy, self.max_deepth)

        return alfa_beta.get_move()