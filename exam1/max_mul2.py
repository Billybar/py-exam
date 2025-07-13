def max_mul2(lst): # no 0 in lst
    # lst not sorted
    pos_max1 = 0
    pos_max2 = 0
    neg_max1 = 0
    neg_max2 = 0

    for num in lst:
        # for positive int
        if num > 0 and num > pos_max1:
            pos_max2 = pos_max1
            pos_max1 = num
        elif num > 0 and num > pos_max2:
            pos_max2 = num

        # for negative int
        if num < 0 and num < neg_max1:
            neg_max2 = neg_max1
            neg_max1 = num
        elif num < 0 and num < neg_max2:
            neg_max2 =num

    pos_num = pos_max1*pos_max2
    neg_num = neg_max1*neg_max2

    if pos_num == 0 and neg_num == 0:
        return pos_max1*neg_max1

    return max(pos_max1*pos_max2, neg_max1*neg_max2)

import math

# (Paste the corrected max_mul2 function here if running tests separately)

print("--- Test Cases for max_mul2 ---")

# Test Case 1: Mixed numbers, max product from two positives
# Based on the problem's example, assuming the example had a typo and meant 6*5=30
# If the example [5,6,3,-4] -> 24 (6*4=24) is taken literally, it implies 4 is in the list, which it isn't.
# Standard interpretation for max product will yield 30 for [5,6,3,-4].
list1 = [5, 6, 3, -4]
expected1 = 30 # (6 * 5)
result1 = max_mul2(list1)
print(f"Test Case 1: max_mul2({list1}) = {result1} (Expected: {expected1}) -> {'PASS' if result1 == expected1 else 'FAIL'}")

# Test Case 2: Mixed numbers, max product from two negatives
list2 = [-2, 7, 1, -4]
expected2 = 8 # ((-4) * (-2))
result2 = max_mul2(list2)
print(f"Test Case 2: max_mul2({list2}) = {result2} (Expected: {expected2}) -> {'PASS' if result2 == expected2 else 'FAIL'}")

# Test Case 3: Only two elements, one positive, one negative
list3 = [2, -4]
expected3 = -8 # (2 * -4)
result3 = max_mul2(list3)
print(f"Test Case 3: max_mul2({list3}) = {result3} (Expected: {expected3}) -> {'PASS' if result3 == expected3 else 'FAIL'}")

# Test Case 4: Only positive numbers
list4 = [1, 2, 3, 10, 5]
expected4 = 50 # (10 * 5)
result4 = max_mul2(list4)
print(f"Test Case 4: max_mul2({list4}) = {result4} (Expected: {expected4}) -> {'PASS' if result4 == expected4 else 'FAIL'}")

# Test Case 5: Only negative numbers
list5 = [-1, -2, -5, -10]
expected5 = 50 # ((-5) * (-10))
result5 = max_mul2(list5)
print(f"Test Case 5: max_mul2({list5}) = {result5} (Expected: {expected5}) -> {'PASS' if result5 == expected5 else 'FAIL'}")

# Test Case 6: List with minimum length (2 positive)
list6 = [7, 9]
expected6 = 63 # (7 * 9)
result6 = max_mul2(list6)
print(f"Test Case 6: max_mul2({list6}) = {result6} (Expected: {expected6}) -> {'PASS' if result6 == expected6 else 'FAIL'}")

# Test Case 7: List with minimum length (2 negative)
list7 = [-7, -9]
expected7 = 63 # ((-7) * (-9))
result7 = max_mul2(list7)
print(f"Test Case 7: max_mul2({list7}) = {result7} (Expected: {expected7}) -> {'PASS' if result7 == expected7 else 'FAIL'}")

# Test Case 8: List with minimum length (1 positive, 1 negative)
list8 = [10, -3]
expected8 = -30 # (10 * -3)
result8 = max_mul2(list8)
print(f"Test Case 8: max_mul2({list8}) = {result8} (Expected: {expected8}) -> {'PASS' if result8 == expected8 else 'FAIL'}")

# Test Case 9: Larger mixed list
list9 = [100, -1, 5, -10, 20, -2, 3]
expected9 = 2000 # (100 * 20)
result9 = max_mul2(list9)
print(f"Test Case 9: max_mul2({list9}) = {result9} (Expected: {expected9}) -> {'PASS' if result9 == expected9 else 'FAIL'}")

# Test Case 10: Mixed list where two largest negatives give the overall max
list10 = [1, 2, -10, -20, 3]
expected10 = 200 # ((-10) * (-20))
result10 = max_mul2(list10)
print(f"Test Case 10: max_mul2({list10}) = {result10} (Expected: {expected10}) -> {'PASS' if result10 == expected10 else 'FAIL'}")