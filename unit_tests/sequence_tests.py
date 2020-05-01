from unit_tests.common import expect, is_none, is_arithmetic_sequnce
from game.sequence import Sequence

def search_with_startidx_equals_zero():
    sequence = Sequence([2, 4, 6, 7, 11], 3)

    res = sequence.search(1, 0)
    expect(-1, res)

    res = sequence.search(5, 0)
    expect(-1, res)

    res = sequence.search(8, 0)
    expect(-1, res)

    res = sequence.search(13, 0)
    expect(-1, res)

    res = sequence.search(2, 0)
    expect(0, res)

    res = sequence.search(6, 0)
    expect(2, res)

    res = sequence.search(11, 0)
    expect(4, res)

def search_startidx_tests():
    sequence = Sequence([2, 4, 6, 7, 11], 3)

    res = sequence.search(2, 1)
    expect(-1, res)

    res = sequence.search(7, 1)
    expect(3, res)

    res = sequence.search(7, 3)
    expect(3, res)

    res = sequence.search(7, 4)
    expect(-1, res)

def find_arithmethic_sequence_for_k_grather_than_n():
    seq = Sequence([1], 2)
    res = seq.find_arithmethic_sequence()
    is_none(res)

    seq = Sequence([1, 2], 3)
    res = seq.find_arithmethic_sequence()
    is_none(res)

    seq = Sequence([1, 2], 4)
    res = seq.find_arithmethic_sequence()
    is_none(res)

def find_arithmethic_sequence_for_k_equals_two():
    seq = Sequence([1], 2)
    res = seq.find_arithmethic_sequence()
    is_none(res)

    seq = Sequence([1, 2], 2)
    res = seq.find_arithmethic_sequence()
    is_arithmetic_sequnce(res, 1, 1)

    seq = Sequence([1, 2, 3], 2)
    res = seq.find_arithmethic_sequence()
    is_arithmetic_sequnce(res, 1, 1)

def find_arithmethic_sequence_tests():
    seq = Sequence([1, 2, 3], 3)
    res = seq.find_arithmethic_sequence()
    is_arithmetic_sequnce(res, 1, 1)

    seq = Sequence([0, 3, 4, 5], 3)
    res = seq.find_arithmethic_sequence()
    is_arithmetic_sequnce(res, 3, 1)

    seq = Sequence([1, 3, 4, 5], 4)
    res = seq.find_arithmethic_sequence()
    is_none(res)

    seq = Sequence([1, 3, 4, 5, 6], 4)
    res = seq.find_arithmethic_sequence()
    is_arithmetic_sequnce(res, 3, 1)

    seq = Sequence([1, 2, 4, 5, 6, 7, 10], 4)
    res = seq.find_arithmethic_sequence()
    is_arithmetic_sequnce(res, 1, 3)

def is_term_tests():
    seq = Sequence([1, 2, 4], 3)
    res = seq.is_term()
    expect(False, res)

    seq = Sequence([1, 2, 3], 3)
    res = seq.is_term()
    expect(True, res)

def sequence_tests():
    search_with_startidx_equals_zero()
    search_startidx_tests()

    find_arithmethic_sequence_for_k_grather_than_n()
    find_arithmethic_sequence_for_k_equals_two()
    find_arithmethic_sequence_tests()

    is_term_tests()

    