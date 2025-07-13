#  list[start:stop:step]
from re import Match


def find(lst, value):
    """
    Finds the position of a value in a list using recursion.
    Returns the index of the value if found, otherwise -1.
    """
    if not lst:  # Base case 1: List is empty, value not found
        return -1

    if lst[0] == value:  # Base case 2: Value found at the current head
        return 0
    else:
        # Recursive step: Search in the rest of the list
        # If value is found in the tail, adjust its index for the original list
        result_in_tail = find(lst[1:], value)

        if result_in_tail == -1:  # Value not found in the tail either
            return -1
        else:  # Value found in the tail, adjust its index for the original list
            return 1 + result_in_tail

def match_width(lst,k,total):
    # return True if there is 2 vals in list such that: abs(a+b) = total and abs(index(a) - index(b)) = k
    if k >= len(lst):
        return False
    if lst[0] + lst[k] == total:
        return True

    return match_width(lst[1:], k,total)



print("--- Test Cases for match_width ---")

# Test Case 1: Basic positive match - CORRECTED EXPECTED VALUE TO FALSE
# No pair (lst[i], lst[i+k]) will sum to abs(70) for k=2
# (10, 30) -> abs(40) != 70
# (20, 40) -> abs(60) != 70
# (30, 50) -> abs(80) != 70
list1 = [10, 20, 30, 40, 50]
k1 = 2
total1 = 70
expected1 = False  # Corrected: It was mistakenly True before.
result1 = match_width(list1, k1, total1)
print(
    f"Test Case 1: {list1}, k={k1}, total={total1} -> {result1} (Expected: {expected1}) {'PASS' if result1 == expected1 else 'FAIL'}")

# Test Case 2: Basic negative match
list2 = [1, 2, 3, 4, 5]
k2 = 1
total2 = 10  # No pair sums to 10 with k=1
expected2 = False
result2 = match_width(list2, k2, total2)
print(
    f"Test Case 2: {list2}, k={k2}, total={total2} -> {result2} (Expected: {expected2}) {'PASS' if result2 == expected2 else 'FAIL'}")

# Test Case 3: Match with negative numbers (abs sum)
# (5, 3) from original indices 1 and 4. Diff is 3, sum is 8.
# Current function checks (lst[i], lst[i+k])
# For [1, 5, 2, 8, 3], k=3:
#   i=0: (1, 8) -> abs(1+8) = 9 != 8
#   i=1: (5, 3) -> abs(5+3) = 8 == 8. This should return True.
list3a = [1, 5, 2, 8, 3]
k3a = 3
total3a = 8  # abs(5 + 3) = 8
expected3a = True
result3a = match_width(list3a, k3a, total3a)
print(
    f"Test Case 3a: {list3a}, k={k3a}, total={total3a} -> {result3a} (Expected: {expected3a}) {'PASS' if result3a == expected3a else 'FAIL'}")

# Test Case 4: k is too large for the list
list4 = [10, 20, 30]
k4 = 3  # len(lst) is 3. k=3. len(lst) <= k (3 <= 3) is True. Should return False.
total4 = 30
expected4 = False
result4 = match_width(list4, k4, total4)
print(
    f"Test Case 4: {list4}, k={k4}, total={total4} -> {result4} (Expected: {expected4}) {'PASS' if result4 == expected4 else 'FAIL'}")

# Test Case 5: k is exactly len(lst)-1 (first and last elements match)
list5 = [1, 2, 3, 4]
k5 = 3  # len(lst) is 4. k=3. 4 <= 3 is False.
# Checks abs(lst[0]+lst[3]) = abs(1+4) = 5.
total5 = 5
expected5 = True
result5 = match_width(list5, k5, total5)
print(
    f"Test Case 5: {list5}, k={k5}, total={total5} -> {result5} (Expected: {expected5}) {'PASS' if result5 == expected5 else 'FAIL'}")

# Test Case 6: List with single element (k will be too large)
list6 = [100]
k6 = 0  # len(lst) is 1. k=0. 1 <= 0 is False.
# Check abs(lst[0] + lst[0]) = abs(100 + 100) = 200.
total6 = 200
expected6 = True  # If k=0 is interpreted as "same element" then True
result6 = match_width(list6, k6, total6)
print(
    f"Test Case 6: {list6}, k={k6}, total={total6} -> {result6} (Expected: {expected6}) {'PASS' if result6 == expected6 else 'FAIL'}")

# Test Case 7: Empty list
list7 = []
k7 = 1
total7 = 10
expected7 = False
result7 = match_width(list7, k7, total7)
print(
    f"Test Case 7: {list7}, k={k7}, total={total7} -> {result7} (Expected: {expected7}) {'PASS' if result7 == expected7 else 'FAIL'}")

# Test Case 8 (k=0): With the current `match_width` function, if k=0:
# For list [5, 10, 15], k=0:
# Call 1: lst=[5,10,15], k=0. len(lst) (3) <= k (0) is False.
#   abs(lst[0]+lst[0]) = abs(5+5) = 10. If total=10, True.
#   If total is not 10, then recurse.
list8_orig = [5, 10, 15]
k8_orig = 0
total8_orig = 10
expected8_orig = True  # Corrected: It should be True because abs(5+5)=10
result8_orig = match_width(list8_orig, k8_orig, total8_orig)
print(
    f"Test Case 8: {list8_orig}, k={k8_orig}, total={total8_orig} -> {result8_orig} (Expected: {expected8_orig}) {'PASS' if result8_orig == expected8_orig else 'FAIL'}")

list8c = [5, 10, 15]
k8c = 0
total8c = 20  # abs(10+10) = 20
expected8c = True
result8c = match_width(list8c, k8c, total8c)
print(
    f"Test Case 8c: {list8c}, k={k8c}, total={total8c} -> {result8c} (Expected: {expected8c}) {'PASS' if result8c == expected8c else 'FAIL'}")

list8d = [5, 10, 15]
k8d = 0
total8d = 30  # abs(15+15) = 30
expected8d = True
result8d = match_width(list8d, k8d, total8d)
print(
    f"Test Case 8d: {list8d}, k={k8d}, total={total8d} -> {result8d} (Expected: {expected8d}) {'PASS' if result8d == expected8d else 'FAIL'}")

list8e = [5, 10, 15]
k8e = 0
total8e = 50  # No match
expected8e = False
result8e = match_width(list8e, k8e, total8e)
print(
    f"Test Case 8e: {list8e}, k={k8e}, total={total8e} -> {result8e} (Expected: {expected8e}) {'PASS' if result8e == expected8e else 'FAIL'}")


print("--- Test Cases for find ---")

# Test 1: Value at the beginning
my_list_1 = [10, 20, 30, 40, 50]
value_1 = 10
expected_1 = 0
result_1 = find(my_list_1, value_1)
print(f"find({my_list_1}, {value_1}) = {result_1} (Expected: {expected_1}) -> {'PASS' if result_1 == expected_1 else 'FAIL'}")

# Test 2: Value in the middle
my_list_2 = [10, 20, 30, 40, 50]
value_2 = 30
expected_2 = 2
result_2 = find(my_list_2, value_2)
print(f"find({my_list_2}, {value_2}) = {result_2} (Expected: {expected_2}) -> {'PASS' if result_2 == expected_2 else 'FAIL'}")

# Test 3: Value at the end
my_list_3 = [10, 20, 30, 40, 50]
value_3 = 50
expected_3 = 4
result_3 = find(my_list_3, value_3)
print(f"find({my_list_3}, {value_3}) = {result_3} (Expected: {expected_3}) -> {'PASS' if result_3 == expected_3 else 'FAIL'}")

# Test 4: Value not in list
my_list_4 = [10, 20, 30, 40, 50]
value_4 = 99
expected_4 = -1
result_4 = find(my_list_4, value_4)
print(f"find({my_list_4}, {value_4}) = {result_4} (Expected: {expected_4}) -> {'PASS' if result_4 == expected_4 else 'FAIL'}")

# Test 5: Empty list
my_list_5 = []
value_5 = 5
expected_5 = -1
result_5 = find(my_list_5, value_5)
print(f"find({my_list_5}, {value_5}) = {result_5} (Expected: {expected_5}) -> {'PASS' if result_5 == expected_5 else 'FAIL'}")

# Test 6: Single element list - found
my_list_6 = [7]
value_6 = 7
expected_6 = 0
result_6 = find(my_list_6, value_6)
print(f"find({my_list_6}, {value_6}) = {result_6} (Expected: {expected_6}) -> {'PASS' if result_6 == expected_6 else 'FAIL'}")

# Test 7: Single element list - not found
my_list_7 = [7]
value_7 = 8
expected_7 = -1
result_7 = find(my_list_7, value_7)
print(f"find({my_list_7}, {value_7}) = {result_7} (Expected: {expected_7}) -> {'PASS' if result_7 == expected_7 else 'FAIL'}")

# Test 8: List with duplicates (finds the first occurrence)
my_list_8 = [1, 2, 2, 3]
value_8 = 2
expected_8 = 1
result_8 = find(my_list_8, value_8)
print(f"find({my_list_8}, {value_8}) = {result_8} (Expected: {expected_8}) -> {'PASS' if result_8 == expected_8 else 'FAIL'}")

# Test 9: Larger list (still prone to recursion depth for very large inputs)
# Uncomment the following to test with a slightly larger list, but be aware of recursion limits.
# For very large lists (e.g., 10000+ elements), this will still likely fail with RecursionError.
# Python's default recursion limit is usually around 1000 or 3000.
# import sys
# sys.setrecursionlimit(2000) # You can temporarily increase, but it's not a true solution for large inputs.
# large_list = list(range(1000))
# value_large = 999
# expected_large = 999
# result_large = find(large_list, value_large)
# print(f"find(large_list, {value_large}) = {result_large} (Expected: {expected_large}) -> {'PASS' if result_large == expected_large else 'FAIL'}")