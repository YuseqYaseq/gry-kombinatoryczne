from game.game import Game
from unit_tests.common import expect

def find_longest_ap_tests():
    def assert_find_longest_ap(element_list, expected_value):
        res = Game._find_longest_ap(element_list)
        expect(res, expected_value)

    def list_empty():
        assert_find_longest_ap([], 0)
    
    def list_len_equal_to_one():
        assert_find_longest_ap([5], 1)

    def list_len_equal_to_two():
        assert_find_longest_ap([2, 5], 2)

    def list_len_equal_to_three_with_max_ap():
        assert_find_longest_ap([1, 5, 9], 3)

    def list_len_equal_to_three_with_ap_two():
        assert_find_longest_ap([1, 5, 10], 2)
    
    def list_len_greater_than_three_with_max_ap():
        assert_find_longest_ap([1, 3, 5, 7, 9, 11], 6)
    
    def list_len_greater_than_three_with_different_aps():
        assert_find_longest_ap([1, 3, 5, 6, 11, 16], 4)
    
    list_empty()
    list_len_equal_to_one()
    list_len_equal_to_two()
    list_len_equal_to_three_with_max_ap()
    list_len_equal_to_three_with_ap_two()
    list_len_greater_than_three_with_max_ap()
    list_len_greater_than_three_with_different_aps()

def game_tests():
    find_longest_ap_tests()