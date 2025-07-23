def magic_list(mat: list[list[int]]) -> bool:
    if not mat:
        # An empty matrix, by definition, has no frame or inner elements.
        # So, the sum of both is 0, making them equal.
        return True

    rows = len(mat)
    cols = len(mat[0])

    # If the matrix is too small to have an "inner" part (e.g., less than 3x3)
    # then all elements are considered part of the frame.
    # In this specific case, for the sums to be equal, the total sum of all elements must be 0,
    # because the inner sum would be 0.
    if rows < 3 or cols < 3:
        total_sum = 0
        for r_idx in range(rows):
            for c_idx in range(cols):
                total_sum += mat[r_idx][c_idx]
        return total_sum == 0

    frame_sum = 0
    inner_sum = 0

    # Calculate the sum of the frame elements and inner elements
    for r_idx in range(rows):
        for c_idx in range(cols):
            # Check if the current element is on the border (frame)
            if r_idx == 0 or r_idx == rows - 1 or c_idx == 0 or c_idx == cols - 1:
                frame_sum += mat[r_idx][c_idx]
            else:
                inner_sum += mat[r_idx][c_idx]

    return frame_sum == inner_sum


# Test cases from the problem description
mat1 = [[1, 1, 1, 1],
        [1, 3, 3, 1],
        [1, 3, 3, 1],
        [1, 1, 1, 1]]

mat2 = [[1, 2, 1, 1, 2],
        [1, 4, 4, 4, 1],
        [3, 3, 4, 3, 1],
        [2, 3, 1, 1, 2]]

# Additional test cases
mat_not_magic_frame_greater = [[1, 1, 1],
                               [1, 10, 1],
                               [1, 1, 1]]

mat_not_magic_inner_greater = [[1, 1, 1],
                               [1, 100, 1],
                               [1, 1, 1]]

mat_3x3_magic = [[1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1]]  # Frame sum = 8, Inner sum = 0. Not magic.

mat_3x3_true_magic = [[1, 1, 1],
                      [1, 8, 1],
                      [1, 1, 1]]  # Frame sum = 8, Inner sum = 8. Magic.

mat_small_all_frame_zero_sum = [[0, 0], [0, 0]]  # Should be True
mat_small_all_frame_non_zero_sum = [[1, 1], [1, 1]]  # Should be False

mat_empty = []  # Should be True
mat_single_row = [[1, 2, 3]]  # Should be False (sum of 1,2,3 is 6, inner is 0)
mat_single_col = [[1], [2], [3]]  # Should be False (sum of 1,2,3 is 6, inner is 0)
mat_2x2 = [[1, 2], [3, 4]]  # Should be False (sum of 1,2,3,4 is 10, inner is 0)

print(f"mat1 is magic: {magic_list(mat1)}")
print(f"mat2 is magic: {magic_list(mat2)}")
print(f"mat_not_magic_frame_greater is magic: {magic_list(mat_not_magic_frame_greater)}")
print(f"mat_not_magic_inner_greater is magic: {magic_list(mat_not_magic_inner_greater)}")
print(f"mat_3x3_magic is magic: {magic_list(mat_3x3_magic)}")
print(f"mat_3x3_true_magic is magic: {magic_list(mat_3x3_true_magic)}")
print(f"mat_small_all_frame_zero_sum is magic: {magic_list(mat_small_all_frame_zero_sum)}")
print(f"mat_small_all_frame_non_zero_sum is magic: {magic_list(mat_small_all_frame_non_zero_sum)}")
print(f"mat_empty is magic: {magic_list(mat_empty)}")
print(f"mat_single_row is magic: {magic_list(mat_single_row)}")
print(f"mat_single_col is magic: {magic_list(mat_single_col)}")
print(f"mat_2x2 is magic: {magic_list(mat_2x2)}")