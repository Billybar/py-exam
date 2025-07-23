def is_serpentine(mat):
    if not mat:
        return False

    # Now we know mat is not empty. Check if the first row is empty.
    if not mat[0]:
        return False

    rows = len(mat)
    cols = len(mat[0])

    if rows != cols:
        return False
    if mat[0][0] != 1:
        return False

    expected_value = 1
    for r in range(rows):
        if r % 2 == 0:  # Even rows (0, 2, 4...) move left to right
            for c in range(cols):
                if mat[r][c] != expected_value:
                    return False
                expected_value += 1
        else:  # Odd rows (1, 3, 5...) move right to left
            for c in range(cols - 1, -1, -1):
                if mat[r][c] != expected_value:
                    return False
                expected_value += 1

    # If all conditions are met and no mismatches were found, it's a serpentine list
    return True

# --- Test Cases ---

def run_tests():
    """
    Runs various test cases for the is_serpentine function.
    """
    print("Running tests for is_serpentine function...\n")

    # Example from the document (5x5 serpentine matrix)
    serpentine_example = [
        [1, 2, 3, 4, 5],
        [10, 9, 8, 7, 6],
        [11, 12, 13, 14, 15],
        [20, 19, 18, 17, 16],
        [21, 22, 23, 24, 25]
    ]
    print(f"Test Case 1 (Serpentine Example):\n{serpentine_example}")
    assert is_serpentine(serpentine_example) == True, "Test Case 1 Failed: Serpentine example should be True"
    print("Result: True (Correct)\n")

    # Test Case 2: Not square
    not_square = [
        [1, 2, 3],
        [6, 5, 4]
    ]
    print(f"Test Case 2 (Not Square):\n{not_square}")
    assert is_serpentine(not_square) == False, "Test Case 2 Failed: Not square should be False"
    print("Result: False (Correct)\n")

    # Test Case 3: Does not start with 1
    starts_wrong = [
        [0, 1, 2],
        [5, 4, 3],
        [6, 7, 8]
    ]
    print(f"Test Case 3 (Starts with 0):\n{starts_wrong}")
    assert is_serpentine(starts_wrong) == False, "Test Case 3 Failed: Does not start with 1 should be False"
    print("Result: False (Correct)\n")

    # Test Case 4: Incorrect sequence
    incorrect_sequence = [
        [1, 2, 3],
        [6, 5, 7],  # 7 is wrong, should be 4
        [8, 9, 10]
    ]
    print(f"Test Case 4 (Incorrect Sequence):\n{incorrect_sequence}")
    assert is_serpentine(incorrect_sequence) == False, "Test Case 4 Failed: Incorrect sequence should be False"
    print("Result: False (Correct)\n")

    # Test Case 5: 1x1 serpentine
    single_element = [[1]]
    print(f"Test Case 5 (1x1 Serpentine):\n{single_element}")
    assert is_serpentine(single_element) == True, "Test Case 5 Failed: 1x1 should be True"
    print("Result: True (Correct)\n")

    # Test Case 6: 2x2 serpentine
    two_by_two = [
        [1, 2],
        [4, 3]
    ]
    print(f"Test Case 6 (2x2 Serpentine):\n{two_by_two}")
    assert is_serpentine(two_by_two) == True, "Test Case 6 Failed: 2x2 should be True"
    print("Result: True (Correct)\n")

    # Test Case 7: Empty list
    empty_list = []
    print(f"Test Case 7 (Empty List):\n{empty_list}")
    assert is_serpentine(empty_list) == False, "Test Case 7 Failed: Empty list should be False"
    print("Result: False (Correct)\n")

    # Test Case 8: Empty inner list
    empty_inner_list = [[]]
    print(f"Test Case 8 (Empty Inner List):\n{empty_inner_list}")
    assert is_serpentine(empty_inner_list) == False, "Test Case 8 Failed: Empty inner list should be False"
    print("Result: False (Correct)\n")

    # Test Case 9: Non-consecutive values
    non_consecutive = [
        [1, 2, 3],
        [7, 6, 5], # 7 is wrong, should be 4
        [8, 9, 10]
    ]
    print(f"Test Case 9 (Non-consecutive values):\n{non_consecutive}")
    assert is_serpentine(non_consecutive) == False, "Test Case 9 Failed: Non-consecutive values should be False"
    print("Result: False (Correct)\n")

    print("All tests passed!")

# To run the tests, uncomment the line below:
run_tests()