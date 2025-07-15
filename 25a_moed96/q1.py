def sort_by_reminder(lst, m):
    current_sorted_index = 0    # until what index the lst is sorted so far

    # Iterate through each possible remainder from 0 to m-1
    for r in range(m):              # 0(1) as m is constant

        # For each remainder 'r', iterate through the unsorted part of the list
        # to find elements that have this remainder.
        i = current_sorted_index
        while i < len(lst):         # o(n)
            if lst[i] % m == r:
                # If an element with the current remainder 'r' is found,
                # swap it with the element at 'current_sorted_index'.
                # This moves the element to its correct sorted position.
                temp = lst[current_sorted_index]
                lst[current_sorted_index] = lst[i]
                lst[i] = temp
                current_sorted_index += 1
            i += 1
    return lst



def test_sort_by_reminder():
    print("Running tests for sort_by_reminder...\n")

    # Test Case 1: Basic functionality with m = 4
    # Expected order: elements % 4 == 0, then % 4 == 1, then % 4 == 2, then % 4 == 3
    # Original: [10, 5, 6, 22, 13, 14]
    # Remainders for m=4:
    # 10 % 4 = 2
    # 5 % 4 = 1
    # 6 % 4 = 2
    # 22 % 4 = 2
    # 13 % 4 = 1
    # 14 % 4 = 2
    # Expected (sorted by remainder, relative order within remainder group preserved due to in-place swaps):
    # Remainder 0: None
    # Remainder 1: 5, 13
    # Remainder 2: 10, 6, 22, 14
    # Remainder 3: None
    # So the output should be [5, 13, 10, 6, 22, 14]
    #
    # The example given in the problem statement for `lst=[22,14,6,10,5,13]` returning `[10,5,6,22,13,14]`
    # for an unspecified `m` is confusing and doesn't seem to strictly follow the "relative order within remainder group is preserved"
    # interpretation if m=4.
    # However, if we assume m=4, and we prioritize the numbers that appeared earliest in the original list within each remainder group,
    # the function's in-place swapping behavior naturally handles this.
    # Let's re-evaluate the provided example [22, 14, 6, 10, 5, 13] -> [10, 5, 6, 22, 13, 14]
    # If m=2, 0-remainder: 22, 14, 6, 10. 1-remainder: 5, 13
    # Output could be [22, 14, 6, 10, 5, 13]
    # [cite_start]The provided example output for [22, 14, 6, 10, 5, 13] is [10, 5, 6, 22, 13, 14][cite: 78].
    # Let's verify what m would make this output possible.
    # If m=4, and the example output is [10, 5, 6, 22, 13, 14]:
    # 10%4=2, 5%4=1, 6%4=2, 22%4=2, 13%4=1, 14%4=2.
    # This implies that the elements with remainder 1 (5, 13) are grouped together, and elements with remainder 2 (10, 6, 22, 14) are grouped.
    # But the order [10, 5, 6, 22, 13, 14] for m=4 doesn't strictly follow the remainder order (2, 1, 2, 2, 1, 2).
    # It might mean that the example given in the document is a bit generalized or for a different 'm'.
    # For my test cases, I will strictly follow the rule: "At the beginning of the list will appear all numbers divisible by m without remainder,
    # [cite_start]followed by all numbers divisible by m with remainder 1, etc."[cite: 74].

    list1 = [10, 5, 6, 22, 13, 14]
    m1 = 4
    expected1 = [5, 13, 6, 22, 10, 14] # Elements with remainder 1: [5, 13], then remainder 2: [10, 6, 22, 14]
    result1 = sort_by_reminder(list1.copy(), m1) # Use a copy to avoid modifying original list for other tests
    print(f"Test Case 1: List: {list1}, m: {m1}")
    print(f"Expected: {expected1}")
    print(f"Result:   {result1}")
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Test Case 1 Passed.\n")

    # Test Case 2: No elements with remainder 0, or elements already partially sorted
    list2 = [7, 1, 9, 3, 5]
    m2 = 2
    # 7%2=1, 1%2=1, 9%2=1, 3%2=1, 5%2=1
    expected2 = [7, 1, 9, 3, 5] # All have remainder 1, so relative order should be preserved
    result2 = sort_by_reminder(list2.copy(), m2)
    print(f"Test Case 2: List: {list2}, m: {m2}")
    print(f"Expected: {expected2}")
    print(f"Result:   {result2}")
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Test Case 2 Passed.\n")

    # Test Case 3: Empty list
    list3 = []
    m3 = 5
    expected3 = []
    result3 = sort_by_reminder(list3.copy(), m3)
    print(f"Test Case 3: List: {list3}, m: {m3}")
    print(f"Expected: {expected3}")
    print(f"Result:   {result3}")
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Test Case 3 Passed.\n")

    # Test Case 4: List with single element
    list4 = [42]
    m4 = 7
    expected4 = [42] # 42 % 7 = 0
    result4 = sort_by_reminder(list4.copy(), m4)
    print(f"Test Case 4: List: {list4}, m: {m4}")
    print(f"Expected: {expected4}")
    print(f"Result:   {result4}")
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Test Case 4 Passed.\n")

    # Test Case 5: m = 1 (all remainders are 0)
    list5 = [10, 20, 30, 40]
    m5 = 1
    expected5 = [10, 20, 30, 40]
    result5 = sort_by_reminder(list5.copy(), m5)
    print(f"Test Case 5: List: {list5}, m: {m5}")
    print(f"Expected: {expected5}")
    print(f"Result:   {result5}")
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Test Case 5 Passed.\n")

    # Test Case 6: Larger numbers, m > max(list)
    list6 = [3, 8, 1, 5, 2]
    m6 = 10
    # 3%10=3, 8%10=8, 1%10=1, 5%10=5, 2%10=2
    # Expected: 1, 2, 3, 5, 8 (sorted by remainder values)
    expected6 = [1, 2, 3, 5, 8]
    result6 = sort_by_reminder(list6.copy(), m6)
    print(f"Test Case 6: List: {list6}, m: {m6}")
    print(f"Expected: {expected6}")
    print(f"Result:   {result6}")
    assert result6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Test Case 6 Passed.\n")

    # Test Case 7: Numbers with remainder 0, then others
    list7 = [15, 3, 10, 7, 20]
    m7 = 5
    # 15%5=0, 3%5=3, 10%5=0, 7%5=2, 20%5=0
    # Expected: [15, 10, 20, 7, 3] (0-remainders: 15, 10, 20; 2-remainder: 7; 3-remainder: 3)
    expected7 = [15, 10, 20, 7, 3]
    result7 = sort_by_reminder(list7.copy(), m7)
    print(f"Test Case 7: List: {list7}, m: {m7}")
    print(f"Expected: {expected7}")
    print(f"Result:   {result7}")
    assert result7 == expected7, f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Test Case 7 Passed.\n")

    # Test Case 8: Duplicate numbers
    list8 = [4, 1, 8, 3, 4, 2]
    m8 = 4
    # 4%4=0, 1%4=1, 8%4=0, 3%4=3, 4%4=0, 2%4=2
    # Expected: [4, 8, 4, 1, 2, 3] (0-remainders: 4, 8, 4; 1-remainder: 1; 2-remainder: 2; 3-remainder: 3)
    expected8 = [4, 8, 4, 1, 2, 3]
    result8 = sort_by_reminder(list8.copy(), m8)
    print(f"Test Case 8: List: {list8}, m: {m8}")
    print(f"Expected: {expected8}")
    print(f"Result:   {result8}")
    assert result8 == expected8, f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Test Case 8 Passed.\n")


# Call the test function
test_sort_by_reminder()