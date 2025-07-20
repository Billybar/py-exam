# section a
def is_sub_list_non_seq(lst, sub):

    if not sub:
        return True

    elif not lst:
        return False

    elif sub[0] == lst[0]:
        return is_sub_list_non_seq(lst[1:], sub[1:])

    else: # sub[0] != lst[0]
        return is_sub_list_non_seq(lst[1:], sub)


# section b
def is_sub_list_seq(lst, sub):

    if not sub:
        return True

    elif not lst:
        return False

    # Option 1: Try to match the sublist starting from the current lst[0].
    # This involves a strict sequential check using the helper function.
    match_from_current = False
    if sub[0] == lst[0]:
        match_from_current = _is_sub_list_seq(lst[1:], sub[1:])

    # Option 2: Try to match the sublist by skipping the current lst[0].
    # This involves recursively calling is_sub_list_seq on the rest of lst
    # with the full sub, allowing the sequence to start later in lst.
    match_by_skipping_current = is_sub_list_seq(lst[1:], sub)

    # If either option finds a match, return True.
    return match_from_current or match_by_skipping_current



def _is_sub_list_seq(lst, sub):
    if not sub:
        return True

    elif not lst:
        return False

    elif sub[0] == lst[0]:
        return _is_sub_list_seq(lst[1:], sub[1:])

    else: # sub[0] != lst[0] -> no seq
        return False


def run_tests():
    print("Running tests for is_sub_list_non_seq (Section A):")
    # Test cases from the exam document
    assert is_sub_list_non_seq([5,2,8,1,3,4,10], [4,10]) == True, "Non-seq Test 1 Failed"
    assert is_sub_list_non_seq([5,2,8,1,3,4,10], [2,3,10]) == True, "Non-seq Test 2 Failed"
    assert is_sub_list_non_seq([5,2,8,1,3,4,10], [3,1,10]) == False, "Non-seq Test 3 Failed (order)"
    assert is_sub_list_non_seq([5,2,8,1,3,4,10], [5,8,1,11]) == False, "Non-seq Test 4 Failed (element not found)"
    assert is_sub_list_non_seq([5,2,8,1,3,4,10], []) == True, "Non-seq Test 5 Failed (empty sub)"

    # Additional edge cases for non-sequential
    assert is_sub_list_non_seq([], []) == True, "Non-seq Test 6 Failed (both empty)"
    assert is_sub_list_non_seq([], [1,2]) == False, "Non-seq Test 7 Failed (empty lst, non-empty sub)"
    assert is_sub_list_non_seq([1,2,3,4,5], [1,3,5]) == True, "Non-seq Test 8 Failed (sparse match)"
    assert is_sub_list_non_seq([1,2,3,4,5], [1,2,3,4,5]) == True, "Non-seq Test 9 Failed (exact match)"
    assert is_sub_list_non_seq([1,2,3], [1,2,3,4]) == False, "Non-seq Test 10 Failed (sub longer than lst)"
    assert is_sub_list_non_seq([1,1,2,3], [1,3]) == True, "Non-seq Test 11 Failed (duplicate in lst)"
    assert is_sub_list_non_seq([1,2,3,4,5], [5]) == True, "Non-seq Test 12 Failed (single last element)"
    assert is_sub_list_non_seq([1,2,3,4,5], [1]) == True, "Non-seq Test 13 Failed (single first element)"
    print("All is_sub_list_non_seq tests passed!")

    print("\nRunning tests for is_sub_list_seq (Section B):")
    # Test cases from the exam document
    assert is_sub_list_seq([5,2,8,1,3,4,10], [4,10]) == True, "Seq Test 1 Failed (not sequential)"
    assert is_sub_list_seq([5,2,8,1,3,4,10], [2,4,10]) == False, "Seq Test 2 Failed (not sequential)"
    assert is_sub_list_seq([5,2,8,1,3,4,10], []) == True, "Seq Test 3 Failed (empty sub)"

    # Additional examples for sequential
    assert is_sub_list_seq([1,2,3,4,5], [2,3,4]) == True, "Seq Test 4 Failed (middle sequence)"
    assert is_sub_list_seq([1,2,3,4,5], [1,2,3,4,5]) == True, "Seq Test 5 Failed (full list sequence)"
    assert is_sub_list_seq([1,2,3,4,5], [1,3]) == False, "Seq Test 6 Failed (non-sequential within seq check)"
    assert is_sub_list_seq([1,2,3,4,5,2,3,4,5], [2,3,4]) == True, "Seq Test 7 Failed (duplicate sequence in lst)"
    assert is_sub_list_seq([1,2,3,4,5,2,3,4,5], [3,4,5]) == True, "Seq Test 8 Failed (duplicate sequence in lst, starting later)"
    assert is_sub_list_seq([1,2,3,4,5], [0]) == False, "Seq Test 9 Failed (element not found)"
    assert is_sub_list_seq([1,2,3,4,5], [5]) == True, "Seq Test 10 Failed (single last element)"
    assert is_sub_list_seq([1,2,3,4,5], [1]) == True, "Seq Test 11 Failed (single first element)"
    assert is_sub_list_seq([1,2,3,4,5], [4,5]) == True, "Seq Test 12 Failed (end sequence)"
    assert is_sub_list_seq([1,2,3,4,5], [1,2]) == True, "Seq Test 13 Failed (start sequence)"

    # Edge cases for sequential
    assert is_sub_list_seq([], []) == True, "Seq Test 14 Failed (both empty)"
    assert is_sub_list_seq([], [1,2]) == False, "Seq Test 15 Failed (empty lst, non-empty sub)"
    assert is_sub_list_seq([1,2,3], [1,2,3,4]) == False, "Seq Test 16 Failed (sub longer than lst)"
    assert is_sub_list_seq([1,1,2,3], [1,2,3]) == True, "Seq Test 17 Failed (duplicate start in lst, first match)"
    assert is_sub_list_seq([1,1,2,3], [1,1,2]) == True, "Seq Test 18 Failed (duplicate sublist)"

    print("All is_sub_list_seq tests passed!")

if __name__ == "__main__":
    run_tests()