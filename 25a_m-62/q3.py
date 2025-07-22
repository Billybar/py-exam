
def find(lst, value):
    # Base case 1: If the list is empty, the value cannot be found.
    if not lst:
        return -1

    # Base case 2: If the first element is the value, return its index (0 relative to current sublist).
    if lst[0] == value:
        return 0

    # Recursive step: Search in the rest of the list.
    # If the value is found in the rest of the list, adjust its index by adding 1.
    # If not found, sub_problem_result will be -1, and we return -1.
    sub_problem_result = find(lst[1:], value)
    if sub_problem_result != -1:
        return 1 + sub_problem_result
    else:
        return -1


def match_width(lst,total,k):

    # if cannot be k = 0 then:
    if k == 0:
        return False

    if k >= len(lst):
        return False

    if not lst:
        return False

    if lst[0] + lst[k] == total:
        return True

    return match_width(lst[1:], total, k)

# Test cases for find (Question 3, Section A)
print("\n--- Testing find ---")

# Example 1 from the problem description
lst_find1 = [8, 2, 3, 11, 5, 10, 7]
value_find1 = 11
expected_find1 = 3
print(f"List: {lst_find1}, Value: {value_find1}, Expected: {expected_find1}, Got: {find(lst_find1, value_find1)}")
assert find(lst_find1, value_find1) == expected_find1, f"find Test 1 Failed: Expected {expected_find1}, Got {find(lst_find1, value_find1)}"

# Example 2 from the problem description
lst_find2 = [8, 2, 3, 11, 5, 10, 7]
value_find2 = 4
expected_find2 = -1
print(f"List: {lst_find2}, Value: {value_find2}, Expected: {expected_find2}, Got: {find(lst_find2, value_find2)}")
assert find(lst_find2, value_find2) == expected_find2, f"find Test 2 Failed: Expected {expected_find2}, Got {find(lst_find2, value_find2)}"

# Additional test case: value at the beginning
lst_find_start = [100, 2, 3]
value_find_start = 100
expected_find_start = 0
print(f"List: {lst_find_start}, Value: {value_find_start}, Expected: {expected_find_start}, Got: {find(lst_find_start, value_find_start)}")
assert find(lst_find_start, value_find_start) == expected_find_start, f"find Test 3 Failed: Expected {expected_find_start}, Got {find(lst_find_start, value_find_start)}"

# Additional test case: value at the end
lst_find_end = [1, 2, 300]
value_find_end = 300
expected_find_end = 2
print(f"List: {lst_find_end}, Value: {value_find_end}, Expected: {expected_find_end}, Got: {find(lst_find_end, value_find_end)}")
assert find(lst_find_end, value_find_end) == expected_find_end, f"find Test 4 Failed: Expected {expected_find_end}, Got {find(lst_find_end, value_find_end)}"

# Additional test case: empty list
lst_find_empty = []
value_find_empty = 5
expected_find_empty = -1
print(f"List: {lst_find_empty}, Value: {value_find_empty}, Expected: {expected_find_empty}, Got: {find(lst_find_empty, value_find_empty)}")
assert find(lst_find_empty, value_find_empty) == expected_find_empty, f"find Test 5 Failed: Expected {expected_find_empty}, Got {find(lst_find_empty, value_find_empty)}"

# Additional test case: value not in list
lst_find_not_in = [1, 2, 3]
value_find_not_in = 4
expected_find_not_in = -1
print(f"List: {lst_find_not_in}, Value: {value_find_not_in}, Expected: {expected_find_not_in}, Got: {find(lst_find_not_in, value_find_not_in)}")
assert find(lst_find_not_in, value_find_not_in) == expected_find_not_in, f"find Test 6 Failed: Expected {expected_find_not_in}, Got {find(lst_find_not_in, value_find_not_in)}"

print("All find tests passed!")


# Test cases for match_width (Question 3, Section B)
print("\n--- Testing match_width ---")

# Example 1 from the problem description
lst_mw1 = [8, 2, 3, 11, 5, 10, 7]
total_mw1 = 15
k_mw1 = 1
expected_mw1 = True # 10 (index 5) + 5 (index 4) = 15, abs(5-4) = 1
print(f"List: {lst_mw1}, Total: {total_mw1}, k: {k_mw1}, Expected: {expected_mw1}, Got: {match_width(lst_mw1, total_mw1, k_mw1)}")
assert match_width(lst_mw1, total_mw1, k_mw1) == expected_mw1, f"match_width Test 1 Failed: Expected {expected_mw1}, Got {match_width(lst_mw1, total_mw1, k_mw1)}"

# Example 2 from the problem description
lst_mw2 = [8, 2, 3, 11, 5, 10, 7]
total_mw2 = 15
k_mw2 = 6
expected_mw2 = True # 8 (index 0) + 7 (index 6) = 15, abs(0-6) = 6
print(f"List: {lst_mw2}, Total: {total_mw2}, k: {k_mw2}, Expected: {expected_mw2}, Got: {match_width(lst_mw2, total_mw2, k_mw2)}")
assert match_width(lst_mw2, total_mw2, k_mw2) == expected_mw2, f"match_width Test 2 Failed: Expected {expected_mw2}, Got {match_width(lst_mw2, total_mw2, k_mw2)}"

# Example 3 from the problem description
# lst_mw3 = [8, 2, 3, 11, 5, 10, 7]
# total_mw3 = 12
# k_mw3 = 2
# expected_mw3 = False # 2 (index 1) + 10 (index 5) = 12, but abs(1-5) = 4 != 2
# print(f"List: {lst_mw3}, Total: {total_mw3}, k: {k_mw3}, Expected: {expected_mw3}, Got: {match_width(lst_mw3, total_mw3, k_mw3)}")
# assert match_width(lst_mw3, total_mw3, k_mw3) == expected_mw3, f"match_width Test 3 Failed: Expected {expected_mw3}, Got {match_width(lst_mw3, total_mw3, k_mw3)}"

# Example 4 from the problem description
lst_mw4 = [8, 2, 3, 11, 5, 10, 7]
total_mw4 = 11
k_mw4 = 2
expected_mw4 = False # No pair sums to 11
print(f"List: {lst_mw4}, Total: {total_mw4}, k: {k_mw4}, Expected: {expected_mw4}, Got: {match_width(lst_mw4, total_mw4, k_mw4)}")
assert match_width(lst_mw4, total_mw4, k_mw4) == expected_mw4, f"match_width Test 4 Failed: Expected {expected_mw4}, Got {match_width(lst_mw4, total_mw4, k_mw4)}"

# Additional test case: k = 0 (same element, not allowed if distinct elements are implied)
# Assuming "two values (not necessarily adjacent)" implies distinct values at different indices.
lst_mw_k0 = [1, 2, 3]
total_mw_k0 = 2
k_mw_k0 = 0
expected_mw_k0 = False
print(f"List: {lst_mw_k0}, Total: {total_mw_k0}, k: {k_mw_k0}, Expected: {expected_mw_k0}, Got: {match_width(lst_mw_k0, total_mw_k0, k_mw_k0)}")
assert match_width(lst_mw_k0, total_mw_k0, k_mw_k0) == expected_mw_k0, f"match_width Test 5 Failed: Expected {expected_mw_k0}, Got {match_width(lst_mw_k0, total_mw_k0, k_mw_k0)}"

# Additional test case: empty list
lst_mw_empty = []
total_mw_empty = 10
k_mw_empty = 1
expected_mw_empty = False
print(f"List: {lst_mw_empty}, Total: {total_mw_empty}, k: {k_mw_empty}, Expected: {expected_mw_empty}, Got: {match_width(lst_mw_empty, total_mw_empty, k_mw_empty)}")
assert match_width(lst_mw_empty, total_mw_empty, k_mw_empty) == expected_mw_empty, f"match_width Test 6 Failed: Expected {expected_mw_empty}, Got {match_width(lst_mw_empty, total_mw_empty, k_mw_empty)}"

# Additional test case: single element list
lst_mw_single = [5]
total_mw_single = 5
k_mw_single = 0
expected_mw_single = False
print(f"List: {lst_mw_single}, Total: {total_mw_single}, k: {k_mw_single}, Expected: {expected_mw_single}, Got: {match_width(lst_mw_single, total_mw_single, k_mw_single)}")
assert match_width(lst_mw_single, total_mw_single, k_mw_single) == expected_mw_single, f"match_width Test 7 Failed: Expected {expected_mw_single}, Got {match_width(lst_mw_single, total_mw_single, k_mw_single)}"

# Additional test case: pair at far ends
lst_mw_far_ends = [1, 0, 0, 0, 0, 10]
total_mw_far_ends = 11
k_mw_far_ends = 5
expected_mw_far_ends = True # 1 (index 0) + 10 (index 5) = 11, abs(0-5) = 5
print(f"List: {lst_mw_far_ends}, Total: {total_mw_far_ends}, k: {k_mw_far_ends}, Expected: {expected_mw_far_ends}, Got: {match_width(lst_mw_far_ends, total_mw_far_ends, k_mw_far_ends)}")
assert match_width(lst_mw_far_ends, total_mw_far_ends, k_mw_far_ends) == expected_mw_far_ends, f"match_width Test 8 Failed: Expected {expected_mw_far_ends}, Got {match_width(lst_mw_far_ends, total_mw_far_ends, k_mw_far_ends)}"

# Additional test case: no pair satisfies k
lst_mw_no_k_revised = [1, 2, 6, 8, 10]
total_mw_no_k_revised = 12
k_mw_no_k_revised = 1
expected_mw_no_k_revised = False
print(f"List: {lst_mw_no_k_revised}, Total: {total_mw_no_k_revised}, k: {k_mw_no_k_revised}, Expected: {expected_mw_no_k_revised}, Got: {match_width(lst_mw_no_k_revised, total_mw_no_k_revised, k_mw_no_k_revised)}")
assert match_width(lst_mw_no_k_revised, total_mw_no_k_revised, k_mw_no_k_revised) == expected_mw_no_k_revised, f"match_width Test 9 Failed: Expected {expected_mw_no_k_revised}, Got {match_width(lst_mw_no_k_revised, total_mw_no_k_revised, k_mw_no_k_revised)}"

print("All match_width tests passed!")