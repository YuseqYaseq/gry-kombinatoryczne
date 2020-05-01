from unit_tests.common import expect, is_none, is_arithmetic_sequnce, sequence_contains
from game.sequence import Sequence
from game.alfa_beta import AlfaBeta, max_value


def create_terminal_sequence_tests():
    ab = AlfaBeta([1, 2, 3], [0, 0, 0], 3, 1, 2)
    seq = ab.create_terminal_sequence(1)
    sequence_contains([], seq)

    ab = AlfaBeta([1, 2, 3], [0, 1, 0], 3, 1, 2)
    seq = ab.create_terminal_sequence(1)
    sequence_contains([2], seq)

    ab = AlfaBeta([1, 2, 3], [0, 1, 1], 3, 1, 2)
    seq = ab.create_terminal_sequence(1)
    sequence_contains([2, 3], seq)

    ab = AlfaBeta([1, 2, 3], [0, 1, 0], 3, 1, 2)
    seq = ab.create_terminal_sequence(2)
    sequence_contains([], seq)

    ab = AlfaBeta([1, 2, 3], [0, 1, 2], 3, 1, 2)
    seq = ab.create_terminal_sequence(2)
    sequence_contains([3], seq)


def create_evalute_sequence_tests():
    ab = AlfaBeta([1, 2, 3], [0, 0, 0], 3, 1, 2)
    seq = ab.create_evalute_sequence(1)
    sequence_contains([1, 2, 3], seq)

    ab = AlfaBeta([1, 2, 3], [0, 1, 0], 3, 1, 2)
    seq = ab.create_evalute_sequence(1)
    sequence_contains([1, 2, 3], seq)

    ab = AlfaBeta([1, 2, 3], [0, 1, 1], 3, 1, 2)
    seq = ab.create_evalute_sequence(1)
    sequence_contains([1, 2, 3], seq)

    ab = AlfaBeta([1, 2, 3], [0, 1, 0], 3, 1, 2)
    seq = ab.create_evalute_sequence(2)
    sequence_contains([1, 3], seq)

    ab = AlfaBeta([1, 2, 3], [0, 1, 2], 3, 1, 2)
    seq = ab.create_evalute_sequence(2)
    sequence_contains([1, 3], seq)


def calculate_terminal_node_value_tests():
    ab = AlfaBeta([1, 2, 3], [0, 0, 0], 2, 1, 2)

    res = ab.calculate_terminal_node_value(1)
    is_none(res)

    res = ab.calculate_terminal_node_value(2)
    is_none(res)

    ab = AlfaBeta([1, 2, 3, 4], [0, 1, 0, 2], 2, 1, 2)

    res = ab.calculate_terminal_node_value(1)
    is_none(res)

    res = ab.calculate_terminal_node_value(2)
    is_none(res)

    ab = AlfaBeta([1, 2, 3, 4, 5], [1, 1, 2, 2, 2], 3, 1, 2)

    res = ab.calculate_terminal_node_value(1)
    is_none(res)

    res = ab.calculate_terminal_node_value(2)
    expect(-max_value, res)

    ab = AlfaBeta([1, 2, 3, 4, 5], [1, 2, 1, 2, 1], 3, 1, 2)

    res = ab.calculate_terminal_node_value(1)
    expect(max_value, res)

    res = ab.calculate_terminal_node_value(2)
    is_none(res)

    ab = AlfaBeta([1, 2, 3, 4, 5], [1, 2, 1, 2, 1], 3, 2, 1)

    res = ab.calculate_terminal_node_value(1)
    expect(-max_value, res)

    res = ab.calculate_terminal_node_value(2)
    is_none(res)


def evaluate_node_tests():
    ab = AlfaBeta([1, 2, 3], [0, 0, 0], 2, 1, 2)

    res = ab.evaluate_node(1)
    expect(3, res)

    res = ab.evaluate_node(2)
    expect(-3, res)

    ab = AlfaBeta([1, 2, 3, 4], [0, 1, 0, 2], 2, 1, 2)

    res = ab.evaluate_node(1)
    expect(3, res)

    res = ab.evaluate_node(2)
    expect(-3, res)

    ab = AlfaBeta([1, 2, 3, 4, 5], [1, 1, 2, 2, 2], 3, 1, 2)

    res = ab.evaluate_node(1)
    expect(0, res)

    res = ab.evaluate_node(2)
    expect(-1, res)

    ab = AlfaBeta([1, 2, 3, 4, 5], [1, 0, 1, 2, 1], 3, 1, 2)

    res = ab.evaluate_node(1)
    expect(2, res)

    res = ab.evaluate_node(2)
    expect(0, res)

    ab = AlfaBeta([1, 2, 3, 4, 5], [1, 2, 0, 2, 0], 3, 2, 1)

    res = ab.evaluate_node(1)
    expect(-1, res)

    res = ab.evaluate_node(2)
    expect(2, res)

    ab = AlfaBeta([1, 2, 3, 4, 5, 6, 7], [1, 2, 0, 2, 0, 0, 0], 3, 2, 1)

    res = ab.evaluate_node(1)
    expect(-3, res)

    res = ab.evaluate_node(2)
    expect(6, res)


def first_player_chooses_a_winning_move():
    ab = AlfaBeta([1, 2, 3, 4, 5], [2, 0, 1, 1, 2], 3, 1, 2)
    res = ab.get_move()
    expect(1, res)

    ab = AlfaBeta([1, 2, 3, 4, 5], [0, 0, 1, 1, 2], 3, 1, 2)
    res = ab.get_move()
    expect(1, res)


def second_player_chooses_a_winning_move():
    ab = AlfaBeta([1, 2, 3, 4, 5], [1, 0, 2, 2, 1], 3, 2, 1)
    res = ab.get_move()
    expect(1, res)

    ab = AlfaBeta([1, 2, 3, 4, 5], [0, 0, 2, 2, 1], 3, 2, 1)
    res = ab.get_move()
    expect(1, res)


def first_player_chooses_move_to_win():
    ab = AlfaBeta([1, 2, 3, 4, 5, 6, 7], [2, 2, 1, 0, 0, 0, 1], 3, 1, 2)
    res = ab.get_move()
    expect(4, res)


def second_player_chooses_move_to_win():
    ab = AlfaBeta([1, 2, 3, 4, 5, 6, 7], [1, 1, 2, 0, 0, 0, 2], 3, 2, 1)
    res = ab.get_move()
    expect(4, res)


def first_player_blocks_a_winning_move_of_second_player():
    ab = AlfaBeta([1, 2, 3, 4, 5, 6], [0, 0, 0, 2, 2, 1], 3, 1, 2)
    res = ab.get_move()
    expect(2, res)


def second_player_blocks_a_winning_move_of_first_player():
    ab = AlfaBeta([1, 2, 3, 4, 5, 6], [0, 0, 0, 1, 1, 2], 3, 2, 1)
    res = ab.get_move()
    expect(2, res)


def alfa_beta_tests():
    create_terminal_sequence_tests()
    create_evalute_sequence_tests()

    calculate_terminal_node_value_tests()
    evaluate_node_tests()

    first_player_chooses_a_winning_move()
    second_player_chooses_a_winning_move()

    first_player_chooses_move_to_win()
    second_player_chooses_move_to_win()

    first_player_blocks_a_winning_move_of_second_player()
    second_player_blocks_a_winning_move_of_first_player()
