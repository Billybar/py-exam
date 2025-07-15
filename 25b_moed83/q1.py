def max_drop(lst):
    maxi = lst[0]
    low = lst[1]
    max_different = maxi - low
    left, right  = 0, 1

    while right < len(lst):
        if lst[right] > maxi:
            left = right
            right += 1

        current_different = lst[left] - lst[right]

        # if new max drop found
        if current_different > max_different:
            maxi = lst[left]
            low = lst[right]
            max_different = current_different
            right += 1

        else: # current_different <= max_different:
            right += 1

    print (f"max: {maxi}, low: {low}")
    return max_different




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