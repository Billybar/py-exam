import unittest


def maximal_drop(lst):
    if not lst or len(lst) < 2:
        return 0
    
    max_drop = 0
    highest = lst[0]

    for i in range(1, len(lst)):

        # if next higher -> we have new hill
        if lst[i] > highest:
            highest = lst[i]

        # update current drop
        current_drop = highest - lst[i]

        if current_drop > max_drop:
            max_drop = current_drop

    return max_drop


class TestMaximalDrop(unittest.TestCase):

    def test_examples_from_document(self):
        """
        Tests the function against the specific examples provided in the document.
        """
        # Test case 1: The drop is from 27 to 3.
        self.assertEqual(maximal_drop([4, 6, 7, 24, 12, 27, 3, 21, 5]), 24)

        # Test case 2: The drop is from 26 to 1.
        self.assertEqual(maximal_drop([14, 26, 22, 7, 12, 20, 1, 21]), 25)

        # Test case 3: The drop is from 14 to 3.
        self.assertEqual(maximal_drop([14, 5, 7, 3, 22, 12, 15, 27]), 11)

    def test_edge_cases(self):
        """
        Tests various edge cases to ensure the function is robust.
        """
        # An empty list should result in a drop of 0.
        self.assertEqual(maximal_drop([]), 0)

        # A list with a single element has no possible drop.
        self.assertEqual(maximal_drop([100]), 0)

        # A list with all identical numbers has no drop.
        self.assertEqual(maximal_drop([5, 5, 5, 5, 5]), 0)

    def test_list_types(self):
        """
        Tests lists with specific ordering patterns.
        """
        # A strictly increasing list should have no drop.
        self.assertEqual(maximal_drop([10, 20, 30, 40, 50]), 0)

        # In a strictly decreasing list, the max drop is between the first and last elements.
        self.assertEqual(maximal_drop([50, 40, 30, 20, 10]), 40)

        # A list that goes up and then down (peak in the middle).
        self.assertEqual(maximal_drop([1, 50, 2, 40, 3]), 48)

    def test_with_negative_numbers(self):
        """
        Tests the function's ability to handle lists containing negative numbers.
        """
        # Drop from a positive to a negative number.
        self.assertEqual(maximal_drop([10, -5, 8, -10]), 20)

        # Drop between two negative numbers.
        self.assertEqual(maximal_drop([-2, -5, -1, -8]), 7)


# This allows the test to be run from the command line.
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
