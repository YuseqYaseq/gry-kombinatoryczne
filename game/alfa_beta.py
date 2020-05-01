from game.sequence import Sequence

max_value = 999888777666555

class AlfaBeta:

    def __init__(self, values, state, k, player, enemy, max_deepth = None):
        self.values = values
        self.state = state
        self.k = k
        self.player = player
        self.enemy = enemy

        if max_deepth is None:
            self.max_deepth = k
        else:
            self.max_deepth = max_deepth

    def get_move(self):
        alfa = float('-inf')
        beta = float('inf')
        move = None

        for i in range(0, len(self.state)):
            if self.state[i] == 0:
                self.state[i] = self.player

                child_alfa = self.alfa_beta(self.max_deepth - 1, alfa, beta, self.enemy)
                if alfa < child_alfa:
                    alfa = child_alfa
                    move = i

                self.state[i] = 0

                if alfa >= beta:
                    break
        return move

    def alfa_beta(self, deepth, alfa, beta, current_player):
        terminal_value = self.calculate_terminal_node_value(current_player)
        if terminal_value is not None:
            return terminal_value
        if deepth == 0:
            return self.evaluate_node(current_player)

        if current_player != self.player:
            return self.enemy_visits_children(deepth, alfa, beta, current_player)
        else:
            return self.visit_children(deepth, alfa, beta, current_player)

    def visit_children(self, deepth, alfa, beta, current_player):
        for i in range(0, len(self.state)):
            if self.state[i] == 0:
                self.state[i] = current_player

                child_alfa = self.alfa_beta(deepth - 1, alfa, beta, self.enemy)
                alfa = max(alfa, child_alfa)

                self.state[i] = 0

                if alfa >= beta:
                    break
        return alfa

    def enemy_visits_children(self, deepth, alfa, beta, current_player):
        for i in range(0, len(self.state)):
            if self.state[i] == 0:
                self.state[i] = current_player

                child_beta = self.alfa_beta(deepth - 1, alfa, beta, self.player)
                beta = min(beta, child_beta)

                self.state[i] = 0

                if alfa >= beta:
                    break

        return beta

    def evaluate_node(self, current_player):
        sequence = self.create_evalute_sequence(current_player)
        value = sequence.evaluate()
        if current_player == self.player:
            return value
        else:
            return -value

    def calculate_terminal_node_value(self, current_player):
        sequence = self.create_terminal_sequence(current_player)
        is_term = sequence.is_term()
        if is_term:
            if current_player == self.player:
                return max_value
            else:
                return -max_value
        return None

    def create_terminal_sequence(self, player):
        return self.create_sequence(lambda el: el == player)

    def create_evalute_sequence(self, player):
        return self.create_sequence(lambda el: el == player or el == 0)

    def create_sequence(self, element_pred):
        elements = []
        for i in range(0, len(self.state)):
            if element_pred(self.state[i]):
                elements.append(self.values[i])
        return Sequence(elements, self.k)
