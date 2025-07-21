def difference(lst1,lst2):
    diff_lst  = []
    j = 0   # Pointer for lst2
    i = 0   # Pointer for lst1
    while i < len(lst1) and j < len(lst2):
        a_val = lst1[i]
        b_val = lst2[j]

        # If lst1 element is smaller, it's unique to lst1, add to diff_lst
        if a_val < b_val:
            diff_lst.append(lst1[i])
            i += 1

        elif  a_val > b_val:  # maybe lst2 have the same nuber
            j += 1

        # elements are common, skip both
        else:   # a_val == b_val:
            i += 1
            j += 1

    # option 1: i == len(lst1) -> nothing will be added
    # option 2: j == len(lst2) -> add all remaining nums
    # append all remaining lst1 to diff_lst
    for index in range(i,len(lst1)):
        diff_lst.append(lst1[index])

    return diff_lst


# Test cases
def run_tests():
    print("Running tests for difference function...")

    # Example 1 from problem description
    lst1_1 = [-4, 0, 2, 3, 8, 9]
    lst2_1 = [-4, -2, 1, 3, 5, 10, 12]
    expected_1 = [0, 2, 8, 9]
    result_1 = difference(lst1_1, lst2_1)
    print(f"Test 1: lst1={lst1_1}, lst2={lst2_1}")
    print(f"Expected: {expected_1}, Got: {result_1}")
    assert result_1 == expected_1, f"Test 1 Failed: Expected {expected_1}, Got {result_1}"
    print("Test 1 Passed")

    # Example 2 from problem description (all common elements)
    lst1_2 = [1, 4, 5, 10]
    lst2_2 = [-4, -2, 1, 3, 4, 5, 9, 10]
    expected_2 = []
    result_2 = difference(lst1_2, lst2_2)
    print(f"Test 2: lst1={lst1_2}, lst2={lst2_2}")
    print(f"Expected: {expected_2}, Got: {result_2}")
    assert result_2 == expected_2, f"Test 2 Failed: Expected {expected_2}, Got {result_2}"
    print("Test 2 Passed")

    # Test with lst1 being empty
    lst1_3 = []
    lst2_3 = [1, 2, 3]
    expected_3 = []
    result_3 = difference(lst1_3, lst2_3)
    print(f"Test 3: lst1={lst1_3}, lst2={lst2_3}")
    print(f"Expected: {expected_3}, Got: {result_3}")
    assert result_3 == expected_3, f"Test 3 Failed: Expected {expected_3}, Got {result_3}"
    print("Test 3 Passed")

    # Test with lst2 being empty
    lst1_4 = [1, 2, 3]
    lst2_4 = []
    expected_4 = [1, 2, 3]
    result_4 = difference(lst1_4, lst2_4)
    print(f"Test 4: lst1={lst1_4}, lst2={lst2_4}")
    print(f"Expected: {expected_4}, Got: {result_4}")
    assert result_4 == expected_4, f"Test 4 Failed: Expected {expected_4}, Got {result_4}"
    print("Test 4 Passed")

    # Test with no common elements, and lst1 elements greater than lst2 elements
    lst1_5 = [10, 20, 30]
    lst2_5 = [1, 2, 3]
    expected_5 = [10, 20, 30]
    result_5 = difference(lst1_5, lst2_5)
    print(f"Test 5: lst1={lst1_5}, lst2={lst2_5}")
    print(f"Expected: {expected_5}, Got: {result_5}")
    assert result_5 == expected_5, f"Test 5 Failed: Expected {expected_5}, Got {result_5}"
    print("Test 5 Passed")

    # Test with no common elements, and lst2 elements greater than lst1 elements
    lst1_6 = [1, 2, 3]
    lst2_6 = [10, 20, 30]
    expected_6 = [1, 2, 3]
    result_6 = difference(lst1_6, lst2_6)
    print(f"Test 6: lst1={lst1_6}, lst2={lst2_6}")
    print(f"Expected: {expected_6}, Got: {result_6}")
    assert result_6 == expected_6, f"Test 6 Failed: Expected {expected_6}, Got {result_6}"
    print("Test 6 Passed")

    # Test with some common elements and different lengths
    lst1_7 = [1, 3, 5, 7, 9]
    lst2_7 = [2, 3, 4, 7, 8]
    expected_7 = [1, 5, 9]
    result_7 = difference(lst1_7, lst2_7)
    print(f"Test 7: lst1={lst1_7}, lst2={lst2_7}")
    print(f"Expected: {expected_7}, Got: {result_7}")
    assert result_7 == expected_7, f"Test 7 Failed: Expected {expected_7}, Got {result_7}"
    print("Test 7 Passed")

    print("\nAll tests completed.")

# Run the tests
run_tests()
