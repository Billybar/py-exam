import unittest


def _recursive_check_pairs(current_list):
    # Base case: If the list is empty, all pairs have been found
    if not current_list:
        return True

    # Take the first element as the head
    head = current_list[0]
    opposite = -head

    # Find the index of the opposite element in the rest of the list (from index 1 onwards)
    found_idx = -1
    for i in range(1, len(current_list)):
        if current_list[i] == opposite:
            found_idx = i
            break

    # If the opposite element is not found, then a pair is missing
    if found_idx == -1:
        return False
    else:
        # If found, create a new list for the recursive call by excluding
        # the head (current_list[0]) and the found opposite element (current_list[found_idx]).
        # This uses slicing, which creates new list objects for the recursive call,
        # but avoids building an explicit auxiliary list for storage.
        new_list_for_recursion = current_list[1:found_idx] + current_list[found_idx+1:]
        return _recursive_check_pairs(new_list_for_recursion)

def minus_plus(lst):
    # First, check if the list has an even length. If not, it cannot satisfy the condition.
    if len(lst) % 2 != 0:
        return False

    # If the list is empty, it satisfies the conditions (even length, no elements to check)
    if not lst:
        return True

    # Call the recursive helper function to check for pairs
    return _recursive_check_pairs(lst)


class TestMinusPlus(unittest.TestCase):

    def test_even_length_with_pairs(self):
        # Example from the problem: [3, -3] should return True
        self.assertTrue(minus_plus([3, -3]))
        self.assertTrue(minus_plus([-5, 5]))
        self.assertTrue(minus_plus([1, -1, 2, -2]))
        self.assertTrue(minus_plus([-10, 20, 10, -20]))
        self.assertTrue(minus_plus([1, 2, -1, -2])) # Order doesn't matter

    def test_odd_length(self):
        # Example from the problem: [3, -3, 5] should return False (odd length)
        self.assertFalse(minus_plus([3, -3, 5]))
        self.assertFalse(minus_plus([1]))
        self.assertFalse(minus_plus([1, -1, 2]))

    def test_even_length_without_pairs(self):
        # Example from the problem: [3, 5] should return False (3 has no -3)
        self.assertFalse(minus_plus([3, 5]))
        self.assertFalse(minus_plus([1, -2]))
        self.assertFalse(minus_plus([1, 1, -1, 2])) # One '1' has no '-1'
        self.assertFalse(minus_plus([1, -1, 2, 3]))

    def test_empty_list(self):
        # An empty list has even length and no elements to check for pairs
        self.assertTrue(minus_plus([]))

    def test_duplicate_numbers(self):
        self.assertTrue(minus_plus([1, -1, 1, -1]))
        self.assertFalse(minus_plus([1, 1, -1])) # Odd length
        self.assertFalse(minus_plus([1, 1, -1, -1, 2])) # Odd length
        self.assertTrue(minus_plus([1, -1, 2, -2, 3, -3]))

    def test_larger_lists(self):
        self.assertTrue(minus_plus([1, -1, 2, -2, 3, -3, 4, -4, 5, -5]))
        self.assertFalse(minus_plus([1, -1, 2, -2, 3, -3, 4, -4, 5])) # Odd length
        self.assertFalse(minus_plus([1, -1, 2, -2, 3, -4, 5, -5])) # 3 has no -3, 4 has no -4

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)