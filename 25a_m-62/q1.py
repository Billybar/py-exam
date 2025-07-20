def find_pairs(lst, k):
    total_pairs = 0
    left = 0
    right = 1

    # Edge case: a list with fewer than 2 elements cannot form pairs
    if len(lst) < 2:
        return total_pairs

    while right < len(lst):

        # If both pointers are at the same position, move right pointer
        if left == right:
            right += 1
            if right == len(lst):
                break

        diff = lst[right] - lst[left]

        if diff == k:
            total_pairs += 1
            # Move both pointers to find the next pair
            left += 1
            right += 1

        elif diff < k:
            # Need a larger difference, move right pointer
            right += 1

        else: # diff > k
            # Need a smaller difference, move left pointer
            left +=1

    return total_pairs


import unittest

class TestFindPairs(unittest.TestCase):

    def test_example_one(self):
        # Example from the problem description: k=2, expected 4 pairs
        lst = [-7, -3, 0, 1, 3, 5, 12, 14, 17, 19, 25, 30]
        k = 2
        self.assertEqual(find_pairs(lst, k), 4)

    def test_example_two(self):
        # Example from the problem description: k=6, expected 2 pairs
        lst = [-7, -3, 0, 1, 3, 5, 12, 14, 17, 19, 25, 30]
        k = 6
        self.assertEqual(find_pairs(lst, k), 2)

    def test_example_three(self):
        # Example from the problem description: k=23, expected 0 pairs
        lst = [-7, -3, 0, 1, 3, 5, 12, 14, 17, 19, 25, 30]
        k = 23
        self.assertEqual(find_pairs(lst, k), 0)

    def test_empty_list(self):
        # Test case with an empty list
        lst = []
        k = 5
        self.assertEqual(find_pairs(lst, k), 0)

    def test_single_element_list(self):
        # Test case with a single-element list
        lst = [10]
        k = 3
        self.assertEqual(find_pairs(lst, k), 0)

    def test_no_pairs(self):
        # List where no pairs have the exact difference
        lst = [1, 5, 10, 15, 20]
        k = 2
        self.assertEqual(find_pairs(lst, k), 0)

    def test_multiple_pairs(self):
        # List with several pairs having the difference
        lst = [1, 2, 3, 4, 5, 6]
        k = 1
        self.assertEqual(find_pairs(lst, k), 5) # (1,2), (2,3), (3,4), (4,5), (5,6)

    def test_negative_numbers(self):
        # List with negative numbers and positive k
        lst = [-5, -3, -1, 1, 3]
        k = 2
        self.assertEqual(find_pairs(lst, k), 4) # (-5,-3), (-3,-1), (-1,1), (1,3)

    def test_zero_in_list(self):
        # List including zero
        lst = [-2, 0, 2, 4]
        k = 2
        self.assertEqual(find_pairs(lst, k), 3) # (-2,0), (0,2), (2,4)

    def test_larger_list(self):
        # A slightly larger list
        lst = [1, 3, 5, 7, 9, 11, 13, 15]
        k = 4
        self.assertEqual(find_pairs(lst, k), 6) # (1,5), (3,7), (5,9), (7,11), (9,13), (11,15) - Mistake in expectation (1,5),(3,7),(5,9),(7,11),(9,13),(11,15) is 6 pairs
        # Correction: (1,5), (3,7), (5,9), (7,11), (9,13), (11,15) = 6 pairs. My bad.

    def test_duplicate_elements_in_test_list_but_problem_states_no_duplicates_in_input(self):
        # The problem states "ממוינת בסדר עולה ממש (כלומר, אין ערכים חוזרים)" meaning strictly increasing, no duplicates.
        # So this test case for duplicates is technically not needed based on the problem statement.
        # However, for robustness, one might consider it if the input guarantee wasn't strict.
        pass

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)