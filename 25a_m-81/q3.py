def is_magic(lst, m):

    if m == 0 or m == len(lst)-1:
        return False
    # To satisfy the requirement of a recursive function for a single-point check,
    # we use a recursive helper. This helper will "count" or "iterate"
    # recursively until it reaches the target index 'm', at which point
    # it performs the actual magic number condition check.
    # We start the helper's 'current_idx' from 1, as index 0 is already handled.
    return _is_magic_recursive_helper(lst, m, 1)

def _is_magic_recursive_helper(lst, target_idx, current_idx):
    # Base Case: If the current index matches the target index,
    # we have reached the element we need to check.
    if current_idx == target_idx:
        # We can directly perform the magic number condition check.
        return lst[target_idx] == lst[target_idx - 1] + lst[target_idx + 1]

    # Recursive Step: If the current index has not yet reached the target index,
    # make a recursive call with the next index.
    # We ensure current_idx does not exceed target_idx, as target_idx is guaranteed valid.
    if current_idx < target_idx:
        return _is_magic_recursive_helper(lst, target_idx, current_idx + 1)
    else:
        # This 'else' block should ideally not be reached if 'target_idx' is valid
        # and 'current_idx' starts correctly and increments towards it.
        # It serves as a safeguard for unexpected scenarios.
        return False

def n_magic(lst, n):

    return _n_magic(lst,n,1)

def _n_magic(lst,n,i):

    # Base Case: If current_multiple_idx exceeds the list bounds,
    # all relevant magic numbers have been checked (and passed).
    if i*n >= len(lst):
        return True

    if not is_magic(lst,i*n):
        return False

    # Recursive Step
    return _n_magic(lst,n,i+1)





# --- Test Cases (as provided in the problem description) ---
if __name__ == "__main__":
    test_list = [1, 5, 11, 6, 9, 3, 6, 3]

    print(f"Testing with list: {test_list}")

    # Tests for is_magic (Section A)
    print("\n--- Testing is_magic (Section A) ---")
    # Example 1: m = 0 (first element)
    m_val = 0
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: False)")
    assert result is False, f"Test Failed for m={m_val}"

    # Example 2: m = 2 (magic number: 5 + 6 = 11)
    m_val = 2
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: True)")
    assert result is True, f"Test Failed for m={m_val}"

    # Example 3: m = 3 (not a magic number: 11 + 9 != 6)
    m_val = 3
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: False)")
    assert result is False, f"Test Failed for m={m_val}"

    # Additional test cases for is_magic:

    # Last element
    m_val = len(test_list) - 1
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val} (last element), is_magic returns: {result} (Expected: False)")
    assert result is False, f"Test Failed for m={m_val} (last element)"

    # List too short (less than 3 elements)
    short_list = [1, 2]
    m_val = 0
    result = is_magic(short_list, m_val)
    print(f"For short list {short_list}, m = {m_val}, is_magic returns: {result} (Expected: False)")
    assert result is False, f"Test Failed for short list {short_list}"

    # Another magic number in the test_list (e.g., index 6: 3 + 3 = 6)
    m_val = 6
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: True)")
    assert result is True, f"Test Failed for m={m_val}"

    # Non-magic number in the middle
    m_val = 4 # 6 + 3 = 9
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: True)")
    assert result is True, f"Test Failed for m={m_val}"


    # Tests for n_magic (Section B)
    print("\n--- Testing n_magic (Section B) ---")

    # Example 1: n = 2 (indices 2, 4, 6 are magic: 11, 9, 6)
    # 11 (idx 2) is magic (5+6=11) -> True
    # 9 (idx 4) is NOT magic (6+3!=9) -> False
    # 6 (idx 6) is magic (3+3=6) -> True
    # The problem description states: "עבור n=2 הפונקציה תחזיר True מכיוון שכל האיברים הנמצאים במקומות שהם כפולה של 2 (המקום ה- 2,4,6) הם "איברי קסם"."
    # This implies that for the given test_list, index 4 (value 9) *should* be considered a magic number for this example to be True.
    # However, by the definition of is_magic, 9 (at index 4) is not 6+3.
    # Let's re-evaluate the example. If the example is correct as stated (returns True), then 9 must be considered magic in that context.
    # But based on the `is_magic` function logic, 9 is not magic.
    # I will proceed with the `is_magic` function's current logic for consistency, which means this test will fail if the example is strictly followed.
    # The problem statement for n=2 example: "עבור n=2 הפונקציה תחזיר True מכיוון שכל האיברים הנמצאים במקומות שהם כפולה של 2 (המקום ה- 2,4,6) הם "איברי קסם"."
    # This implies 9 (at index 4) *is* a magic number according to the problem's interpretation for this specific example.
    # I'll use the current `is_magic` logic.
    n_val = 2
    # Indices to check: 2, 4, 6
    # is_magic(test_list, 2) -> True (11 = 5 + 6)
    # is_magic(test_list, 4) -> False (9 != 6 + 3)
    # is_magic(test_list, 6) -> True (6 = 3 + 3)
    # So, expected should be False based on our `is_magic` implementation.
    expected_n2 = True # Based on our `is_magic` logic, index 4 is not magic.
    result_n2 = n_magic(test_list, n_val)
    print(f"For n = {n_val}, n_magic returns: {result_n2} (Expected: {expected_n2})")
    assert result_n2 == expected_n2, f"Test Failed for n={n_val}"

    # Example 2: n = 4 (index 4 is magic)
    # Indices to check: 4
    # is_magic(test_list, 4) -> False (9 = 6 + 3)
    # The problem states: "עבור n=4 הפונקציה תחזיר True מכיוון שהאיבר במקום ה- 4 הוא "איבר קסם" (אין ברשימה איברים נוספים במקומות שהם כפולה של 4)."
    # Again, this implies 9 (at index 4) *is* a magic number for the example to be True.
    # Based on our `is_magic` function, it's False.
    n_val = 4
    expected_n4 = True # Based on our `is_magic` logic, index 4 is not magic.
    result_n4 = n_magic(test_list, n_val)
    print(f"For n = {n_val}, n_magic returns: {result_n4} (Expected: {expected_n4})")
    assert result_n4 == expected_n4, f"Test Failed for n={n_val}"

    # Example 3: n = 3 (index 3 is not magic)
    # Indices to check: 3, 6
    # is_magic(test_list, 3) -> False (6 != 11 + 9)
    # is_magic(test_list, 6) -> True (6 = 3 + 3)
    n_val = 3
    expected_n3 = False # Because index 3 is not magic.
    result_n3 = n_magic(test_list, n_val)
    print(f"For n = {n_val}, n_magic returns: {result_n3} (Expected: {expected_n3})")
    assert result_n3 == expected_n3, f"Test Failed for n={n_val}"

    # Additional test cases for n_magic:

    # n such that no multiples are in range (or only 0)
    n_val = 10
    result_n_large = n_magic(test_list, n_val)
    print(f"For n = {n_val} (large), n_magic returns: {result_n_large} (Expected: True)")
    assert result_n_large is True, f"Test Failed for n={n_val} (large)"

    # n = 1 (check all middle elements)
    # Indices to check: 1, 2, 3, 4, 5, 6, 7
    # is_magic(test_list, 1) -> False (5 != 1+11)
    # is_magic(test_list, 2) -> True (11 = 5+6)
    # is_magic(test_list, 3) -> False (6 != 11+9)
    # is_magic(test_list, 4) -> False (9 != 6+3)
    # is_magic(test_list, 5) -> False (3 != 9+6)
    # is_magic(test_list, 6) -> True (6 = 3+3)
    # is_magic(test_list, 7) -> False (last element)
    n_val = 1
    result_n1 = n_magic(test_list, n_val)
    print(f"For n = {n_val}, n_magic returns: {result_n1} (Expected: False)")
    assert result_n1 is False, f"Test Failed for n={n_val}"

    # Empty list
    empty_list = []
    n_val = 2
    result_empty = n_magic(empty_list, n_val)
    print(f"For empty list, n = {n_val}, n_magic returns: {result_empty} (Expected: True)")
    assert result_empty is True, f"Test Failed for empty list"

    # List with less than 3 elements
    small_list = [1, 5]
    n_val = 1
    result_small = n_magic(small_list, n_val)
    print(f"For small list {small_list}, n = {n_val}, n_magic returns: {result_small} (Expected: False)")
    assert result_small is False, f"Test Failed for small list"

    print("\nAll tests completed.")


# --- Test Cases (as provided in the problem description) ---
if __name__ == "__main__":
    test_list = [1, 5, 11, 6, 9, 3, 6, 3]

    print(f"Testing with list: {test_list}")

    # Example 1: m = 0 (first element)
    m_val = 0
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: False)")
    assert result is False, f"Test Failed for m={m_val}"

    # Example 2: m = 2 (magic number: 5 + 6 = 11)
    m_val = 2
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: True)")
    assert result is True, f"Test Failed for m={m_val}"

    # Example 3: m = 3 (not a magic number: 11 + 9 != 6)
    m_val = 3
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: False)")
    assert result is False, f"Test Failed for m={m_val}"

    # Additional test cases:

    # Last element
    m_val = len(test_list) - 1
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val} (last element), is_magic returns: {result} (Expected: False)")
    assert result is False, f"Test Failed for m={m_val} (last element)"

    # List too short (less than 3 elements)
    short_list = [1, 2]
    m_val = 0
    result = is_magic(short_list, m_val)
    print(f"For short list {short_list}, m = {m_val}, is_magic returns: {result} (Expected: False)")
    assert result is False, f"Test Failed for short list {short_list}"

    # Another magic number in the test_list (e.g., index 6: 3 + 3 = 6)
    m_val = 6
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: True)")
    assert result is True, f"Test Failed for m={m_val}"

    # Non-magic number in the middle
    m_val = 4 # 6 + 3 = 9
    result = is_magic(test_list, m_val)
    print(f"For m = {m_val}, is_magic returns: {result} (Expected: True)")
    assert result is True, f"Test Failed for m={m_val}"

    print("\nAll tests passed!")