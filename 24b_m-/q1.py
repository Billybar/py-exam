def is_up_down(lst):

    # find pick (if exists)
    i = 1
    while i < len(lst):

        # if the same number -> False
        if lst[i-1] == lst[i]:
            return False

        # if still going up -> continue
        elif lst[i-1] < lst[i]:
            i +=1

        else: # lst[i-1] > lst[i]
            i +=1
            break # we get to the pick


    # check its going down only
    while i < len(lst):

        # if same or going up -> False
        if lst[i-1] <= lst[i]:
            return False
        i+=1

    return True


def test_is_up_down():
    # Example lists given in the problem
    print("Testing is_up_down function...")

    # Examples of strictly increasing then strictly decreasing lists:
    lst1 = [-1, 3, 7, 8, 5]
    print(f"Test Case 1: {lst1} - Expected: True, Got: {is_up_down(lst1)}")
    assert is_up_down(lst1) == True

    lst2 = [2, 8]
    print(f"Test Case 2: {lst2} - Expected: True, Got: {is_up_down(lst2)}")
    assert is_up_down(lst2) == True

    lst3 = [6, 4, 1]
    print(f"Test Case 3: {lst3} - Expected: True, Got: {is_up_down(lst3)}")
    assert is_up_down(lst3) == True

    # Examples of lists that are NOT strictly increasing then strictly decreasing (from problem or derived):
    lst4 = [-1, 3, 7, 8, 5, 6]  # Ends with an increase
    print(f"Test Case 4: {lst4} - Expected: False, Got: {is_up_down(lst4)}")
    assert is_up_down(lst4) == False

    lst5 = [2, 8, 8]  # Not strictly increasing or decreasing at the peak
    print(f"Test Case 5: {lst5} - Expected: False, Got: {is_up_down(lst5)}")
    assert is_up_down(lst5) == False

    lst6 = [6, 4, 1, 2]  # Starts decreasing, then increases
    print(f"Test Case 6: {lst6} - Expected: False, Got: {is_up_down(lst6)}")
    assert is_up_down(lst6) == False

    # Additional test cases for more comprehensive coverage:

    # Edge cases:
    # List that is only strictly increasing
    lst_only_increasing = [1, 2, 3, 4, 5]
    print(f"Test Case 7: {lst_only_increasing} - Expected: True, Got: {is_up_down(lst_only_increasing)}")
    assert is_up_down(lst_only_increasing) == True

    # List that is only strictly decreasing
    lst_only_decreasing = [5, 4, 3, 2, 1]
    print(f"Test Case 8: {lst_only_decreasing} - Expected: True, Got: {is_up_down(lst_only_decreasing)}")
    assert is_up_down(lst_only_decreasing) == True

    # List with two elements, increasing
    lst_two_elements_inc = [1, 5]
    print(f"Test Case 9: {lst_two_elements_inc} - Expected: True, Got: {is_up_down(lst_two_elements_inc)}")
    assert is_up_down(lst_two_elements_inc) == True

    # List with two elements, decreasing
    lst_two_elements_dec = [5, 1]
    print(f"Test Case 10: {lst_two_elements_dec} - Expected: True, Got: {is_up_down(lst_two_elements_dec)}")
    assert is_up_down(lst_two_elements_dec) == True

    # List with duplicate values within increasing part
    lst_dup_inc = [1, 2, 2, 3, 1]
    print(f"Test Case 11: {lst_dup_inc} - Expected: False, Got: {is_up_down(lst_dup_inc)}")
    assert is_up_down(lst_dup_inc) == False

    # List with duplicate values within decreasing part
    lst_dup_dec = [1, 5, 3, 3, 2]
    print(f"Test Case 12: {lst_dup_dec} - Expected: False, Got: {is_up_down(lst_dup_dec)}")
    assert is_up_down(lst_dup_dec) == False

    # List with no peak (all same values, if allowed by problem's specific interpretation)
    # The current implementation of is_up_down would return False for these as they are not *strictly* increasing/decreasing
    lst_all_same = [7, 7, 7, 7]
    print(f"Test Case 13: {lst_all_same} - Expected: False, Got: {is_up_down(lst_all_same)}")
    assert is_up_down(lst_all_same) == False

    # Complex case
    lst_complex_true = [1, 2, 3, 10, 9, 8, 7, 6, 5]
    print(f"Test Case 14: {lst_complex_true} - Expected: True, Got: {is_up_down(lst_complex_true)}")
    assert is_up_down(lst_complex_true) == True

    lst_complex_false = [1, 2, 3, 10, 9, 8, 7, 6, 5, 11]
    print(f"Test Case 15: {lst_complex_false} - Expected: False, Got: {is_up_down(lst_complex_false)}")
    assert is_up_down(lst_complex_false) == False

    print("\nAll tests completed.")

# Run the tests
test_is_up_down()