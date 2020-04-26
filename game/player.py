from random import randint
from typing import List


class Player:

    def get_move(self, nodes: List):
        ret = randint(0, len(nodes)-1)
        while nodes[ret] != 0:
            ret = randint(0, len(nodes)-1)
        return ret
