# section A)
def update_list(lst,value):
    new_lst = []
    value_found = False
    if not lst:
        return []

    return _update_list(lst, value, 0, value_found, new_lst)

def _update_list(lst, value, i, value_found, new_lst):
    # if end of lst -> return new lst
    if i == len(lst):
        return new_lst

    # if value found -> mark and do not add to new lst
    if lst[i] == value and not value_found:
        value_found = True
        return _update_list(lst, value, i+1, value_found, new_lst)

    # add element to new lst
    new_lst.append(lst[i])
    # move to next element
    return _update_list(lst, value, i+1, value_found, new_lst)

# section B)
def equal_lists(lst1, lst2):
    if lst1 == lst2:
        return True
    if len(lst1) != len(lst2):
        return False

    lst1 = update_list(lst1, lst2[0])
    return equal_lists(lst1, lst2[1:])


##########################################################################
#####             TESTS                ########



print("--- Testing update_list ---")

# Test 1: Basic removal of first occurrence
lst1_test1 = [3, 1, 8, 10, 6]
value_test1 = 1
expected_test1 = [3, 8, 10, 6]
result_test1 = update_list(lst1_test1, value_test1)
print(f"List: {lst1_test1}, Value: {value_test1}")
print(f"Expected: {expected_test1}, Got: {result_test1}")
assert result_test1 == expected_test1, f"Test 1 Failed: Expected {expected_test1}, Got {result_test1}"

# Test 2: Value appears more than once, remove only first
lst1_test2 = [4, 3, 1, 3, 8]
value_test2 = 3
expected_test2 = [4, 1, 3, 8]
result_test2 = update_list(lst1_test2, value_test2)
print(f"List: {lst1_test2}, Value: {value_test2}")
print(f"Expected: {expected_test2}, Got: {result_test2}")
assert result_test2 == expected_test2, f"Test 2 Failed: Expected {expected_test2}, Got {result_test2}"

# Test 3: Value not in list
lst1_test3 = [3, 1, 8, 10, 6]
value_test3 = 99
expected_test3 = [3, 1, 8, 10, 6] # Original list should be returned
result_test3 = update_list(lst1_test3, value_test3)
print(f"List: {lst1_test3}, Value: {value_test3}")
print(f"Expected: {expected_test3}, Got: {result_test3}")
assert result_test3 == expected_test3, f"Test 3 Failed: Expected {expected_test3}, Got {result_test3}"

# Test 4: Value at the beginning
lst1_test4 = [1, 3, 8]
value_test4 = 1
expected_test4 = [3, 8]
result_test4 = update_list(lst1_test4, value_test4)
print(f"List: {lst1_test4}, Value: {value_test4}")
print(f"Expected: {expected_test4}, Got: {result_test4}")
assert result_test4 == expected_test4, f"Test 4 Failed: Expected {expected_test4}, Got {result_test4}"

# Test 5: Value at the end
lst1_test5 = [3, 8, 1]
value_test5 = 1
expected_test5 = [3, 8]
result_test5 = update_list(lst1_test5, value_test5)
print(f"List: {lst1_test5}, Value: {value_test5}")
print(f"Expected: {expected_test5}, Got: {result_test5}")
assert result_test5 == expected_test5, f"Test 5 Failed: Expected {expected_test5}, Got {result_test5}"

# Test 6: Empty list
lst1_test6 = []
value_test6 = 5
expected_test6 = []
result_test6 = update_list(lst1_test6, value_test6)
print(f"List: {lst1_test6}, Value: {value_test6}")
print(f"Expected: {expected_test6}, Got: {result_test6}")
assert result_test6 == expected_test6, f"Test 6 Failed: Expected {expected_test6}, Got {result_test6}"

# Test 7: List with one element, which is the value to remove
lst1_test7 = [5]
value_test7 = 5
expected_test7 = []
result_test7 = update_list(lst1_test7, value_test7)
print(f"List: {lst1_test7}, Value: {value_test7}")
print(f"Expected: {expected_test7}, Got: {result_test7}")
assert result_test7 == expected_test7, f"Test 7 Failed: Expected {expected_test7}, Got {result_test7}"

print("All update_list tests passed!")




print("\n--- Testing equal_lists ---")

# Test 1: Lists are permutations
lst1_test1 = [1, 4, 3, 1, 2]
lst2_test1 = [1, 1, 2, 3, 4]
expected_test1 = True # Example from problem [cite: 220]
result_test1 = equal_lists(lst1_test1.copy(), lst2_test1.copy()) # Use .copy() to avoid modifying original lists in subsequent tests
print(f"List1: {lst1_test1}, List2: {lst2_test1}")
print(f"Expected: {expected_test1}, Got: {result_test1}")
assert result_test1 == expected_test1, f"Test 1 Failed: Expected {expected_test1}, Got {result_test1}"

# Test 2: Lists have different lengths
lst1_test2 = [8, 1, 3, 3]
lst2_test2 = [8, 1, 3]
expected_test2 = False # Example from problem [cite: 221]
result_test2 = equal_lists(lst1_test2.copy(), lst2_test2.copy())
print(f"List1: {lst1_test2}, List2: {lst2_test2}")
print(f"Expected: {expected_test2}, Got: {result_test2}")
assert result_test2 == expected_test2, f"Test 2 Failed: Expected {expected_test2}, Got {result_test2}"

# Test 3: Lists are identical (also permutations)
lst1_test3 = [1, 2, 3]
lst2_test3 = [1, 2, 3]
expected_test3 = True
result_test3 = equal_lists(lst1_test3.copy(), lst2_test3.copy())
print(f"List1: {lst1_test3}, List2: {lst2_test3}")
print(f"Expected: {expected_test3}, Got: {result_test3}")
assert result_test3 == expected_test3, f"Test 3 Failed: Expected {expected_test3}, Got {result_test3}"

# Test 4: Lists are permutations with different order
lst1_test4 = [5, 2, 8, 1]
lst2_test4 = [8, 1, 5, 2]
expected_test4 = True
result_test4 = equal_lists(lst1_test4.copy(), lst2_test4.copy())
print(f"List1: {lst1_test4}, List2: {lst2_test4}")
print(f"Expected: {expected_test4}, Got: {result_test4}")
assert result_test4 == expected_test4, f"Test 4 Failed: Expected {expected_test4}, Got {result_test4}"

# Test 5: Lists have same length but different elements
lst1_test5 = [1, 2, 3]
lst2_test5 = [1, 2, 4]
expected_test5 = False
result_test5 = equal_lists(lst1_test5.copy(), lst2_test5.copy())
print(f"List1: {lst1_test5}, List2: {lst2_test5}")
print(f"Expected: {expected_test5}, Got: {result_test5}")
assert result_test5 == expected_test5, f"Test 5 Failed: Expected {expected_test5}, Got {result_test5}"

# Test 6: Empty lists
lst1_test6 = []
lst2_test6 = []
expected_test6 = True
result_test6 = equal_lists(lst1_test6.copy(), lst2_test6.copy())
print(f"List1: {lst1_test6}, List2: {lst2_test6}")
print(f"Expected: {expected_test6}, Got: {result_test6}")
assert result_test6 == expected_test6, f"Test 6 Failed: Expected {expected_test6}, Got {result_test6}"

# Test 7: One empty list, one non-empty
lst1_test7 = [1]
lst2_test7 = []
expected_test7 = False
result_test7 = equal_lists(lst1_test7.copy(), lst2_test7.copy())
print(f"List1: {lst1_test7}, List2: {lst2_test7}")
print(f"Expected: {expected_test7}, Got: {result_test7}")
assert result_test7 == expected_test7, f"Test 7 Failed: Expected {expected_test7}, Got {result_test7}"

# Test 8: Lists with duplicate elements, but one has an extra unique element
lst1_test8 = [1, 2, 2, 3]
lst2_test8 = [1, 2, 3, 4]
expected_test8 = False
result_test8 = equal_lists(lst1_test8.copy(), lst2_test8.copy())
print(f"List1: {lst1_test8}, List2: {lst2_test8}")
print(f"Expected: {expected_test8}, Got: {result_test8}")
assert result_test8 == expected_test8, f"Test 8 Failed: Expected {expected_test8}, Got {result_test8}"

# Test 9: Lists with different counts of duplicate elements
lst1_test9 = [1, 2, 2, 3]
lst2_test9 = [1, 2, 3]
expected_test9 = False # Lengths differ
result_test9 = equal_lists(lst1_test9.copy(), lst2_test9.copy())
print(f"List1: {lst1_test9}, List2: {lst2_test9}")
print(f"Expected: {expected_test9}, Got: {result_test9}")
assert result_test9 == expected_test9, f"Test 9 Failed: Expected {expected_test9}, Got {result_test9}"

# Test 10: Lists with many duplicate elements
lst1_test10 = [1, 1, 2, 2, 3, 3]
lst2_test10 = [3, 2, 1, 3, 2, 1]
expected_test10 = True
result_test10 = equal_lists(lst1_test10.copy(), lst2_test10.copy())
print(f"List1: {lst1_test10}, List2: {lst2_test10}")
print(f"Expected: {expected_test10}, Got: {result_test10}")
assert result_test10 == expected_test10, f"Test 10 Failed: Expected {expected_test10}, Got {result_test10}"


print("All equal_lists tests completed. Review assertions for success/failure.")