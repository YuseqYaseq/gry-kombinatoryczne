from game.player import Player
from game.sequence import Sequence


def get_player_sequence(game, player, k):
    values = []
    for i in range(0, len(game)):
        if game[i] == player:
            values.append(i)
    return Sequence(values, k)


def play(p1, p2, game, k):

    while 0 in game:
        move = p1.get_move(game)
        game[move] = p1.player
        print(game)

        seq = get_player_sequence(game, p1.player, k)
        if seq.is_term():
            print('First player win')
            exit()

        move = p2.get_move(game)
        game[move] = p2.player
        print(game)

        seq = get_player_sequence(game, p2.player, k)
        if seq.is_term():
            print('Second player win')
            exit()

#TODO Change all in the future
#Example
def main():
    k = 3
    n = 10
    player1 = Player(1, 2, k, 3)
    player2 = Player(2, 1, k, 3)
    game = [0 for _ in range(n)]

    play(player1, player2, game, k)


if __name__ == "__main__":
    main()
