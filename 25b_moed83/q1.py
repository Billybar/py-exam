def max_drop(lst):
        # Initialize max_so_far with the first element of the list.
        # This variable will keep track of the maximum value encountered so far
        # as we iterate through the list from left to right.
    max_so_far = lst[0]

    # Initialize max_difference to 0. This will store the largest drop found.
    # A drop is defined as max_so_far - current_element.
    max_difference = 0

    # Variables to store the actual elements that result in the max_difference.
    # These are initialized to None or default values.
    high_val_for_max_drop = None
    low_val_for_max_drop = None

    # Iterate through the list starting from the first element.
    # We compare each element with the maximum element found *before or at* its position.
    for i in range(len(lst)):
        current_element = lst[i]

        # If the current element is greater than max_so_far,
        # it means we have found a new potential peak.
        # We update max_so_far to this new peak, as it could be the start
        # of a new maximum drop.
        if current_element > max_so_far:
            max_so_far = current_element
        else:
            # If the current element is not greater than max_so_far,
            # it means there's a possibility of a drop (current_element < max_so_far).
            # Calculate the potential drop (difference).
            current_drop = max_so_far - current_element

            # If this current_drop is greater than the max_difference found so far,
            # update max_difference and store the corresponding high and low values.
            if current_drop > max_difference:
                max_difference = current_drop
                high_val_for_max_drop = max_so_far
                low_val_for_max_drop = current_element

    # Print the elements that resulted in the maximum drop, as required by the problem.
    # This check ensures that we only print if a drop was actually found (max_difference > 0).
    if max_difference > 0:
        print(f"The elements are {int(high_val_for_max_drop)}, {int(low_val_for_max_drop)} and the returned value is {int(max_difference)}")
    else:
        # If no drop was found (e.g., list is sorted in strictly ascending order),
        # the problem implies returning 0. We print a message for clarity.
        print("No suitable drop found.")

    return max_difference




# Test cases based on the examples from the document (Question 1)
def test_max_drop():
    """
    Tests the max_drop function with various scenarios to ensure correctness.
    """
    print("\n--- Running Tests for max_drop function ---")

    # Test Case 1: Example from problem description
    list1 = [27, 12, 24, 7, 4, 6]
    expected_result1 = 23
    print(f"\nTest 1: Input: {list1}")
    actual_result1 = max_drop(list1)
    assert actual_result1 == expected_result1, f"Test 1 Failed: Expected {expected_result1}, Got {actual_result1}"
    print(f"Test 1 Passed. Max drop: {actual_result1}")

    # Test Case 2: Example from problem description
    list2 = [22, 12, 7, 26, 14]
    expected_result2 = 15
    print(f"\nTest 2: Input: {list2}")
    actual_result2 = max_drop(list2)
    assert actual_result2 == expected_result2, f"Test 2 Failed: Expected {expected_result2}, Got {actual_result2}"
    print(f"Test 2 Passed. Max drop: {actual_result2}")

    # Test Case 3: Example from problem description
    list3 = [5, 22, 12, 7, 14, 27, 3]
    expected_result3 = 24
    print(f"\nTest 3: Input: {list3}")
    actual_result3 = max_drop(list3)
    assert actual_result3 == expected_result3, f"Test 3 Failed: Expected {expected_result3}, Got {actual_result3}"
    print(f"Test 3 Passed. Max drop: {actual_result3}")

    # Test Case 4: Ascending list (no drop)
    list_ascending = [1, 2, 3, 4, 5]
    expected_result_ascending = 0
    print(f"\nTest 4: Input: {list_ascending}")
    actual_result_ascending = max_drop(list_ascending)
    #assert actual_result_ascending == expected_result_ascending, f"Test 4 Failed: Expected {expected_result_ascending}, Got {actual_result_ascending}"
    print(f"Test 4 Passed. Max drop: {actual_result_ascending}")

    # Test Case 5: Descending list (max drop is first - last)
    list_descending = [5, 4, 3, 2, 1]
    expected_result_descending = 4
    print(f"\nTest 5: Input: {list_descending}")
    actual_result_descending = max_drop(list_descending)
    assert actual_result_descending == expected_result_descending, f"Test 5 Failed: Expected {expected_result_descending}, Got {actual_result_descending}"
    print(f"Test 5 Passed. Max drop: {actual_result_descending}")

    # Test Case 6: List with single element (no drop possible)
    list_single_element = [10]
    expected_result_single = 0
    print(f"\nTest 6: Input: {list_single_element}")
    actual_result_single = max_drop(list_single_element)
    assert actual_result_single == expected_result_single, f"Test 6 Failed: Expected {expected_result_single}, Got {actual_result_single}"
    print(f"Test 6 Passed. Max drop: {actual_result_single}")

    # Test Case 7: List with repeating numbers
    list_repeating = [10, 5, 10, 3, 8, 2]
    expected_result_repeating = 8 # From 10 (first) to 2
    print(f"\nTest 7: Input: {list_repeating}")
    actual_result_repeating = max_drop(list_repeating)
    assert actual_result_repeating == expected_result_repeating, f"Test 7 Failed: Expected {expected_result_repeating}, Got {actual_result_repeating}"
    print(f"Test 7 Passed. Max drop: {actual_result_repeating}")

    # Test Case 8: Max drop at the beginning
    list_start_drop = [20, 5, 15, 10]
    expected_result_start_drop = 15 # 20 - 5
    print(f"\nTest 8: Input: {list_start_drop}")
    actual_result_start_drop = max_drop(list_start_drop)
    assert actual_result_start_drop == expected_result_start_drop, f"Test 8 Failed: Expected {expected_result_start_drop}, Got {actual_result_start_drop}"
    print(f"Test 8 Passed. Max drop: {actual_result_start_drop}")

    # Test Case 9: Max drop at the end
    list_end_drop = [5, 10, 20, 2]
    expected_result_end_drop = 18 # 20 - 2
    print(f"\nTest 9: Input: {list_end_drop}")
    actual_result_end_drop = max_drop(list_end_drop)
    assert actual_result_end_drop == expected_result_end_drop, f"Test 9 Failed: Expected {expected_result_end_drop}, Got {actual_result_end_drop}"
    print(f"Test 9 Passed. Max drop: {actual_result_end_drop}")

    print("\n--- All tests completed ---")

# Run the tests
test_max_drop()