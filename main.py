import argparse

from app import App


def get_params():
    parser = argparse.ArgumentParser(description="Play the Szemeredi game")
    parser.add_argument('set_size', metavar='N', type=int, help='Size of the created set.')
    parser.add_argument('k', metavar='k', type=int,
                        help='Length of the monocolor arithmetic sequence needed to win the game')
    parser.add_argument('--depth', nargs='?', default=2,
                        help='Depth of the alpha-beta tree search')
    args = parser.parse_args()
    return args.set_size, args.k, args.depth


def main():
    N, k, d = get_params()
    app = App(N, k, d)
    return app.run()


if __name__ == "__main__":
    main()
