# 3sum sorted style
import unittest


def count_triples(lst, target):
    triplets_counter = 0

    for i in range(len(lst)-2):

        left, right = i+1, len(lst) -1
        while left < right:
            product = lst[i] * lst[left] * lst[right]

            if product == target:
                triplets_counter +=1
                left +=1
                right -=1

            elif product < target:
                left += 1

            else:  # product > target
                right -= 1

    return triplets_counter


class TestCountTriples(unittest.TestCase):

    def test_example_one(self):
        """
        Test case from the exam document: lst=[2,3,4,5,6,7,8,9,10,11,14,18,19,22], num=60
        Expected output: 3 (for triplets (2,3,10), (2,5,6), (3,4,5))
        """
        lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18, 19, 22]
        num = 60
        self.assertEqual(count_triples(lst, num), 3, "Test Case 1 Failed: Should find 3 triplets for num=60")

    def test_example_two(self):
        """
        Test case from the exam document: lst=[2,3,4,5,6,7,8,9,10,11,14,18,19,22], num=80
        Expected output: 2 (for triplets (2,4,10), (2,5,8))
        """
        lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18, 19, 22]
        num = 80
        self.assertEqual(count_triples(lst, num), 2, "Test Case 2 Failed: Should find 2 triplets for num=80")

    def test_example_three(self):
        """
        Test case from the exam document: lst=[2,3,4,5,6,7,8,9,10,11,14,18,19,22], num=20
        Expected output: 0 (no triplets found)
        """
        lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18, 19, 22]
        num = 20
        self.assertEqual(count_triples(lst, num), 0, "Test Case 3 Failed: Should find 0 triplets for num=20")

    def test_empty_list(self):
        """
        Test with an empty list. The problem statement says the list is non-empty,
        but a robust test suite might include this if allowed. Here, it will be skipped
        or noted as outside problem constraints. For the purpose of the problem,
        we assume non-empty.
        """
        # According to[cite: 143], lst is non-empty. So this test case might not be strictly necessary
        # but is good for robustness if the constraints were relaxed.
        # For this context, assuming valid input as per problem.
        pass

    def test_single_triplet(self):
        """
        Test with a list that contains exactly one triplet.
        """
        lst = [1, 2, 3, 4, 5, 6]
        num = 24
        # Expected triplets: (1,4,6) and (2,3,4)
        self.assertEqual(count_triples(lst, num), 2, "Test Case Failed: Should find 2 triplets for num=24")

    def test_no_triplets_large_num(self):
        """
        Test with a num that is too large for any triplet in the list.
        """
        lst = [1, 2, 3, 4, 5]
        num = 100
        self.assertEqual(count_triples(lst, num), 0, "Test Case Failed: Should find 0 triplets for num=100")

    def test_no_triplets_small_num(self):
        """
        Test with a num that is too small for any triplet in the list.
        """
        lst = [10, 20, 30]
        num = 100
        self.assertEqual(count_triples(lst, num), 0, "Test Case Failed: Should find 0 triplets for num=100 with large elements")

    def test_list_with_duplicates_not_allowed(self):
        """
        The problem states the list is strictly ascending (no repeating values).
        This test would violate that, but good to note.
        """
        # According to[cite: 132], lst does not contain repeating values.
        pass

    def test_large_list(self):
        """
        Test with a larger list and a specific number.
        """
        lst = list(range(1, 21)) # [1, 2, ..., 20]
        num = 120
        # Expected triplets for num=120:
        # (1, 6, 20), (1, 8, 15), (1, 10, 12)
        # (2, 3, 20), (2, 4, 15), (2, 5, 12), (2, 6, 10)
        # (3, 4, 10), (3, 5, 8)
        # (4, 5, 6)
        self.assertEqual(count_triples(lst, num), 10, "Test Case Failed: Should find 10 triplets for num=120 with large list")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
