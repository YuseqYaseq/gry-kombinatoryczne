from unit_tests.sequence_tests import sequence_tests
from unit_tests.alfa_beta_tests import alfa_beta_tests
from unit_tests.game_tests import game_tests

def main():
    sequence_tests()
    alfa_beta_tests()
    game_tests()
    print("It's ok")

if __name__ == "__main__":
    main()