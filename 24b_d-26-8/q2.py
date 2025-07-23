import unittest

def is_perfect(lst: list[int]) -> bool:
    n = len(lst)
    if n == 0:
        return False

    # A boolean array to keep track of visited indices.
    # This helps detect cycles and ensures all cells are eventually visited.
    visited = [False] * n
    current_index = 0
    scan_terminated_by_zero = False

    # Loop through the scan path
    while True:
        # 1. Check if the current_index is out of bounds (negative or beyond list length).
        # If it goes out of bounds, the list is not perfect.
        if not (0 <= current_index < n):
            return False

        # 2. Check for cycles: If we visit an index that has already been visited,
        # it means we've entered a loop. If this loop doesn't involve visiting all
        # cells and terminating at a 0, the list is not perfect.
        if visited[current_index]:
            return False

        # Mark the current index as visited.
        visited[current_index] = True

        # Get the jump value from the current cell.
        jump_value = lst[current_index]

        # 3. Check for the termination condition: If the jump_value is 0, the scan ends.
        if jump_value == 0:
            scan_terminated_by_zero = True
            break  # Exit the loop as the scan has terminated

        # Advance to the next index based on the jump_value.
        current_index += jump_value

    # After the loop, evaluate the two main conditions for a perfect list:

    # Condition 2: The scan must have terminated by reaching a cell with value 0.
    # This check is technically redundant if the loop only breaks when jump_value == 0,
    # but it reinforces the explicit requirement.
    if not scan_terminated_by_zero:
        return False

    # Condition 1: All cells of the list must have been scanned.
    # Iterate through the 'visited' array to ensure every index was marked True.
    for i in range(n):
        if not visited[i]:
            return False  # If any cell was not visited, the list is not perfect

    # If all checks pass, the list is perfect.
    return True


class TestIsPerfect(unittest.TestCase):

    def test_perfect_lists(self):
        # Test Case 1: Basic perfect list
        # Path: 0 -> 1 -> 2 (ends on 0). Visited: {0, 1, 2}. All visited.
        self.assertTrue(is_perfect([1, 1, 0]), "Test Case 1 Failed: [1, 1, 0] should be perfect")

        # Test Case 2: Perfect list with a single element
        # Path: 0 (ends on 0). Visited: {0}. All visited.
        self.assertTrue(is_perfect([0]), "Test Case 2 Failed: [0] should be perfect")

        # Test Case 3: Another perfect list
        # Path: 0 -> 1 (ends on 0). Visited: {0, 1}. All visited.
        self.assertTrue(is_perfect([1, 0]), "Test Case 3 Failed: [1, 0] should be perfect")

        # Test Case 4: Longer perfect list
        # Path: 0 -> 1 -> 2 -> 3 (ends on 0). Visited: {0, 1, 2, 3}. All visited.
        self.assertTrue(is_perfect([1, 1, 1, 0]), "Test Case 4 Failed: [1, 1, 1, 0] should be perfect")

        # Test Case 5: List that is NOT perfect because not all cells are visited.
        # Path: 0 -> 2 -> 4 -> 5 (ends on 0). Visited: {0, 2, 4, 5}. Indices 1 and 3 are not visited.
        self.assertFalse(is_perfect([2, 2, 2, 2, 1, 0]), "Test Case 5 Failed: [2, 2, 2, 2, 1, 0] should be non-perfect (not all scanned)")

    def test_non_perfect_lists(self):
        # Test Case 6: Original problem's non-perfect example (scan goes out of bounds)
        # Path: 0 -> 3 -> 8 (out of bounds).
        self.assertFalse(is_perfect([3, 4, 1, 5, 6, 0, 2]), "Test Case 6 Failed: [3, 4, 1, 5, 6, 0, 2] should be non-perfect (out of bounds)")

        # Test Case 7: Empty list (cannot scan all cells or contain 0)
        self.assertFalse(is_perfect([]), "Test Case 7 Failed: [] should be non-perfect")

        # Test Case 8: Scan terminates, but not all cells scanned
        # Path: 0 -> 1 (ends on 0). Visited: {0, 1}. Cells 2, 3 not visited.
        self.assertFalse(is_perfect([1, 0, 1, 1]), "Test Case 8 Failed: [1, 0, 1, 1] should be non-perfect (not all scanned)")

        # Test Case 9: Scan starts at 0, terminates at 0, but not all scanned
        # Path: 0 (ends on 0). Visited: {0}. Cells 1, 2 not visited.
        self.assertFalse(is_perfect([0, 1, 1]), "Test Case 9 Failed: [0, 1, 1] should be non-perfect (not all scanned)")

        # Test Case 10: Scan goes out of bounds
        # Path: 0 -> 1 -> 3 (out of bounds).
        self.assertFalse(is_perfect([1, 2, 1]), "Test Case 10 Failed: [1, 2, 1] should be non-perfect (out of bounds)")

        # Test Case 11: Scan goes out of bounds
        # Path: 0 -> 1 -> 2 -> 3 -> 4 (out of bounds).
        self.assertFalse(is_perfect([1, 1, 1, 1]), "Test Case 11 Failed: [1, 1, 1, 1] should be non-perfect (out of bounds)")

        # Test Case 12: List with all zeros (only first element is scanned)
        # Path: 0 (ends on 0). Visited: {0}. Cells 1, 2 not visited.
        self.assertFalse(is_perfect([0, 0, 0]), "Test Case 12 Failed: [0, 0, 0] should be non-perfect (not all scanned)")

        # Test Case 13: Another case where scan terminates but not all visited
        # Path: 0 -> 1 (ends on 0). Visited: {0, 1}. Cell 2 not visited.
        self.assertFalse(is_perfect([1, 0, 2, 0]), "Test Case 13 Failed: [1, 0, 2, 0] should be non-perfect (not all scanned)")

        # Test Case 14: The problematic example from the problem statement
        # Based on the interpretation that `next_index = current_index + lst[current_index]`,
        # this list is not perfect because the scan goes out of bounds.
        # Path: 0 -> 3 -> 6 (out of bounds for a list of length 6).
        self.assertFalse(is_perfect([3, 0, 1, 3, 4, 2]), "Test Case 14 Failed: [3, 0, 1, 3, 4, 2] should be non-perfect (out of bounds with this interpretation)")


# To run the tests, uncomment the following lines:
# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)
