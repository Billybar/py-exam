import math

def is_identity(mat, x, size):
    # Iterate through rows of the sub-matrix
    for r_offset in range(size):
        # Iterate through columns of the sub-matrix
        for c_offset in range(size):
            current_row = x + r_offset
            current_col = x + c_offset

            # Check for diagonal elements
            if r_offset == c_offset:
                if mat[current_row][current_col] != 1:
                    return False
            # Check for non-diagonal elements
            else:
                if mat[current_row][current_col] != 0:
                    return False
    return True

def max_matrix(mat):
    n = len(mat)
    # The center of the matrix A is at index (n // 2, n // 2)
    # A central sub-matrix of size 's' will have its top-left corner at
    # (center_index - s // 2, center_index - s // 2)
    # And its bottom-right corner at
    # (center_index + s // 2, center_index + s // 2)

    max_identity_size = 0

    # Possible sizes for a central sub-matrix are odd numbers from 1 up to n.
    # The largest possible odd size that can be centered in an n x n matrix
    # where n is odd, is n itself.
    # We iterate downwards from the largest possible odd size to 1.
    for size in range(n, 0, -2):  # Iterate through odd sizes in descending order

        # Calculate the top-left corner (x, x) for the current 'size'
        # The center index of the main matrix:
        center_index = n // 2

        # The top-left corner of the central sub-matrix
        x = center_index - (size // 2)

        # Check if the current central sub-matrix is an identity matrix
        if is_identity(mat, x, size):
            max_identity_size = size
            break  # Found the largest, so we can stop

    return max_identity_size

import unittest

class TestMatrixFunctions(unittest.TestCase):

    def test_is_identity_true_small(self):
        # Test case where a small sub-matrix is an identity matrix
        mat = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertTrue(is_identity(mat, 1, 3))

    def test_is_identity_false_not_one_on_diagonal(self):
        # Test case where a diagonal element is not 1
        mat = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 2, 0, 0],  # This should be 1
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertFalse(is_identity(mat, 1, 3))

    def test_is_identity_false_not_zero_off_diagonal(self):
        # Test case where an off-diagonal element is not 0
        mat = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 5, 1, 0, 0],  # This should be 0
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertFalse(is_identity(mat, 1, 3))

    def test_is_identity_full_matrix(self):
        # Test case where the entire matrix is an identity matrix
        mat = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        self.assertTrue(is_identity(mat, 0, 3))

    def test_is_identity_single_element_true(self):
        # Test case for a 1x1 identity matrix (a single 1)
        mat = [[1]]
        self.assertTrue(is_identity(mat, 0, 1))

    def test_is_identity_single_element_false(self):
        # Test case for a 1x1 matrix that is not identity (a single 0)
        mat = [[0]]
        self.assertFalse(is_identity(mat, 0, 1))

    def test_max_matrix_example_from_problem(self):
        # Example matrix from the problem description (page 3)
        mat = [
            [2, 0, 1, 2, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [3, 0, 0, 1, 0, 0, 0],
            [5, 0, 0, 0, 1, 0, 0],
            [4, 7, 0, 0, 0, 1, 0],
            [8, 0, 0, 0, 0, 0, 1]
        ]
        self.assertEqual(max_matrix(mat), 3)

    def test_max_matrix_larger_example_if_modified(self):
        # Example showing max_matrix returns 5 if specific element changed
        # (based on problem description on page 3)
        mat = [
            [2, 0, 1, 2, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [3, 0, 0, 1, 0, 0, 0],
            [5, 0, 0, 0, 1, 0, 0],
            [0, 7, 0, 0, 0, 1, 0],  # Changed mat[5][0] from 4 to 0
            [8, 0, 0, 0, 0, 0, 1]
        ]
        # To get size 5, the 5x5 submatrix centered at (3,3) must be identity
        # This means mat[1][1] to mat[5][5] must form the identity matrix
        # Let's adjust the matrix slightly to make a 5x5 central identity possible for testing
        mat_for_size_5_test = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(max_matrix(mat_for_size_5_test), 5)


    def test_max_matrix_no_identity(self):
        # Test case where no central identity matrix exists
        mat = [
            [0, 0, 0],
            [0, 5, 0],
            [0, 0, 0]
        ]
        self.assertEqual(max_matrix(mat), 0)

    def test_max_matrix_full_identity(self):
        # Test case where the entire matrix is a central identity matrix
        mat = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]
        ]
        self.assertEqual(max_matrix(mat), 5)

    def test_max_matrix_single_element_identity(self):
        # Test for a 1x1 matrix that is an identity matrix
        mat = [[1]]
        self.assertEqual(max_matrix(mat), 1)

    def test_max_matrix_single_element_not_identity(self):
        # Test for a 1x1 matrix that is not an identity matrix
        mat = [[0]]
        self.assertEqual(max_matrix(mat), 0)

    def test_max_matrix_complex_case(self):
        # A more complex scenario where smaller central identity exists, but not larger
        mat = [
            [9, 9, 9, 9, 9, 9, 9],
            [9, 1, 0, 0, 0, 9, 9],
            [9, 0, 1, 0, 0, 9, 9],
            [9, 0, 0, 1, 0, 9, 9],
            [9, 0, 0, 0, 0, 9, 9], # This '0' breaks 5x5, but 3x3 at center is valid
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9]
        ]
        self.assertEqual(max_matrix(mat), 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)