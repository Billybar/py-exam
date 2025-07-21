def find_median(lst, m):
    """
    Finds the median of a given list of distinct non-negative integers.
    The median is defined as the number in the list such that n/2 elements
    are smaller than it and n/2 elements are larger than it.
    It is assumed that n (the size of the list) is an odd number and at least 3.
    The solution aims for linear time complexity.

    Args:
        lst (list): A list of distinct non-negative integers.
        m (int): The upper bound of the range of values in the list (0-m).

    Returns:
        int: The median of the list.
    """
    n = len(lst)

    # Create a frequency array (or boolean array) to mark the presence of numbers
    # The size of this array should be m+1 to accommodate numbers from 0 to m.
    # Initialize all counts to 0 or all presence to False.
    counts = [0] * (m + 1)  # [cite: 2, 3, 7]

    # Populate the frequency array.
    # This step is linear with respect to n (number of elements in lst)
    # and also with respect to m (if m is much larger than n, but effectively it's min(n, m) operations).
    # Since numbers are distinct and within 0-m, this is efficient.
    for num in lst:  #
        counts[num] = 1  # Mark presence of the number

    # Find the median by iterating through the counts array.
    # The median is the (n/2 + 1)-th smallest element.
    # Since n is odd, n/2 will be integer division, so we need to add 1 to get the correct index.
    # For example, if n=7, n/2 = 3. We need 3 elements smaller, so the 4th element is the median.

    smaller_count = 0
    median_position = n // 2  # The number of elements smaller than the median

    for i in range(m + 1):
        if counts[i] == 1:
            if smaller_count == median_position:  #
                return i
            smaller_count += 1

    return -1  # Should not be reached given the problem constraints


import unittest


# Assuming the find_median function is defined as in the previous responses:
# def find_median(lst, m):
#     n = len(lst)
#     counts = [0] * (m + 1)
#     for num in lst:
#         counts[num] = 1
#     smaller_count = 0
#     median_position = n // 2
#     for i in range(m + 1):
#         if counts[i] == 1:
#             if smaller_count == median_position:
#                 return i
#             smaller_count += 1
#     return -1 # Should not be reached given the problem constraints

class TestFindMedian(unittest.TestCase):

    def test_example_from_problem_description(self):
        """Test case directly from the problem description."""
        lst = [11, 6, 8, 7, 3, 4, 1]
        m = 11
        self.assertEqual(find_median(lst, m), 6)

    def test_smallest_valid_list(self):
        """Test with the smallest valid list size (n=3)."""
        lst = [5, 1, 9]
        m = 10
        self.assertEqual(find_median(lst, m), 5)

    def test_numbers_starting_from_zero(self):
        """Test when numbers in the list include 0."""
        lst = [2, 0, 4]
        m = 5
        self.assertEqual(find_median(lst, m), 2)

    def test_consecutive_numbers(self):
        """Test with a list of consecutive numbers."""
        lst = [10, 8, 9, 7, 6]
        m = 10
        self.assertEqual(find_median(lst, m), 8)

    def test_median_at_higher_end(self):
        """Test where the median is one of the larger values in the list."""
        lst = [1, 2, 3, 4, 10]
        m = 10
        self.assertEqual(find_median(lst, m), 3)

    def test_median_at_lower_end(self):
        """Test where the median is one of the smaller values in the list."""
        lst = [0, 5, 6, 7, 8]
        m = 8
        self.assertEqual(find_median(lst, m), 6)

    def test_larger_list_wider_range(self):
        """Test with a larger list and a wider range of values."""
        lst = [100, 50, 200, 150, 75, 25, 125, 175, 0]
        m = 200
        self.assertEqual(find_median(lst, m), 100)

    def test_list_with_only_zero(self):
        """Test with a list that includes 0 and the median is not 0 (if n > 1)."""
        lst = [0, 10, 20]
        m = 20
        self.assertEqual(find_median(lst, m), 10)

    def test_list_with_max_value_as_median(self):
        """Test case where the median is the maximum value in the range m."""
        lst = [1, 2, 3, 4, 5]
        m = 5  # max value in list is 5
        self.assertEqual(find_median(lst, m), 3)

    def test_list_with_small_m(self):
        """Test with a small 'm' value."""
        lst = [1, 3, 5]
        m = 5
        self.assertEqual(find_median(lst, m), 3)

    def test_list_with_disjoint_numbers(self):
        """Test with numbers that are not clustered."""
        lst = [10, 1, 99, 5, 50]
        m = 100
        self.assertEqual(find_median(lst, m), 10)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)