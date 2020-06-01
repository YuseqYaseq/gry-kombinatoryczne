import argparse

from app import App


def get_params():
    parser = argparse.ArgumentParser(description="Play the Szemeredi game")
    parser.add_argument('set_size', metavar='N', type=int, help='Size of the created set.')
    parser.add_argument('k', metavar='k', type=int,
                        help='Length of the monocolor arithmetic sequence needed to win the game')
    parser.add_argument('min', metavar='min', type=int, help='Minimum value of random numbers appearing in the set')
    parser.add_argument('max', metavar='max', type=int, help='Maximum value of random numbers appearing in the set')
    parser.add_argument('--depth', metavar='d', nargs='?', default=2,
                        help='Depth of the alpha-beta tree search')
    parser.add_argument('--bot-wait-time', metavar='b', nargs='?', default=1,
                        help='Time between each bot move in seconds')
    parser.add_argument('--launch-test', action='store_true',
                        help='Launch 100 tests and count number of won games and moves made by each player.'
                             ' Sets --bot-wait-time to 0.')
    args = parser.parse_args()
    launch_test = bool(args.launch_test)
    bot_wait_time = int(args.bot_wait_time)
    if launch_test:
        bot_wait_time = 0
    return int(args.set_size), int(args.k),\
           int(args.min), int(args.max),\
           int(args.depth), launch_test, bot_wait_time


def main():
    N, k, min, max, d, launch_test, bot_wait_time = get_params()
    app = App(N, k, min, max, d, bot_wait_time)
    if launch_test:
        draws = 0
        p1_wins = 0
        p2_wins = 0
        no_moves = []
        no_games = 100
        for i in range(no_games):
            print(f'\rLaunch game {i+1}/{no_games}', end='')
            winner, no_m = app.run(0)
            if winner == 1:
                p1_wins += 1
            elif winner == 2:
                p2_wins += 1
            else:
                draws += 1
            no_moves.append(no_m)
        print(f'\nPlayer 1 win rate: {100*p1_wins/no_games}%')
        print(f'Player 2 win rate: {100*p2_wins/no_games}%')
        print(f'Draws: {100*draws/no_games}%')
        av = sum(no_moves) / len(no_moves)
        print(f'Average number of moves per game: {av}')
    else:
        winner, no_moves = app.run(10_000)
        if winner == 0:
            print("Draw!")
        elif winner == 1:
            print("Player 1 won!")
        else:
            print("Player 2 won!")


if __name__ == "__main__":
    main()
