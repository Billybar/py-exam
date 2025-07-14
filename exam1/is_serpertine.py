def is_serpertine(mat):
    n = len(mat)

    # col == rows
    if mat[0][0] != 1:
        return False

    if len(mat) != len(mat[0]):
        return False

    expected_value = 1  # The value we expect to find in the current cell

    # Iterate through each row
    for r in range(n):
        if r % 2 == 0:  # Even rows (0, 2, 4, ...): Traverse from left to right
            for c in range(n):
                if mat[r][c] != expected_value:
                    return False  # Value mismatch found
                expected_value += 1  # Increment expected value for the next cell
        else:  # Odd rows (1, 3, 5, ...): Traverse from right to left
            for c in range(n - 1, -1, -1):  # Iterate columns in reverse order
                if mat[r][c] != expected_value:
                    return False  # Value mismatch found
                expected_value += 1  # Increment expected value for the next cell

    # If all conditions are met and no mismatches were found, it's a serpentine list
    return True