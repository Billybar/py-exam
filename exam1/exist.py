def exist(lst,num):
    #return True if num in lst else False
    if not lst:
        return False

    if lst[0] == num:
        return True

    return exist(lst[1:],num)

def find_pair(lst,sum):
    if not lst:
        return False

    if exist(lst[1:],sum - lst[0]):
        return True

    return find_pair(lst[1:], sum)



# --- Test Cases for find_pair ---
print("--- Test Cases for find_pair ---")

# Test Case 1: Basic case - pair exists
list1 = [1, 5, 8, 12]
sum1 = 13  # (1, 12) or (5, 8)
expected1 = True
result1 = find_pair(list1, sum1)
print(
    f"Test Case 1: find_pair({list1}, {sum1}) = {result1} (Expected: {expected1}) -> {'PASS' if result1 == expected1 else 'FAIL'}")

# Test Case 2: Basic case - no pair exists
list2 = [1, 2, 3, 4]
sum2 = 10  # No pair sums to 10
expected2 = False
result2 = find_pair(list2, sum2)
print(
    f"Test Case 2: find_pair({list2}, {sum2}) = {result2} (Expected: {expected2}) -> {'PASS' if result2 == expected2 else 'FAIL'}")

# Test Case 3: Pair with negative numbers
list3 = [-5, 0, 10, 15]
sum3 = 5  # (-5, 10)
expected3 = True
result3 = find_pair(list3, sum3)
print(
    f"Test Case 3: find_pair({list3}, {sum3}) = {result3} (Expected: {expected3}) -> {'PASS' if result3 == expected3 else 'FAIL'}")

# Test Case 4: Sum is 0
list4 = [-3, 0, 3, 7]
sum4 = 0  # (-3, 3)
expected4 = True
result4 = find_pair(list4, sum4)
print(
    f"Test Case 4: find_pair({list4}, {sum4}) = {result4} (Expected: {expected4}) -> {'PASS' if result4 == expected4 else 'FAIL'}")

# Test Case 5: Empty list
list5 = []
sum5 = 10
expected5 = False
result5 = find_pair(list5, sum5)
print(
    f"Test Case 5: find_pair({list5}, {sum5}) = {result5} (Expected: {expected5}) -> {'PASS' if result5 == expected5 else 'FAIL'}")

# Test Case 6: List with single element (cannot form a pair)
list6 = [7]
sum6 = 14  # Needs two elements
expected6 = False
result6 = find_pair(list6, sum6)
print(
    f"Test Case 6: find_pair({list6}, {sum6}) = {result6} (Expected: {expected6}) -> {'PASS' if result6 == expected6 else 'FAIL'}")

# Test Case 7: Crucial test for "two different elements" - pair is (X, X) where X is current_element
# Here, lst[0] (which is 5) needs a complement of 5.
# exist(lst[1:], 5) will be called, and it will find the 5 at index 2.
list7 = [5, 10, 5, 20]
sum7 = 10  # Pair (5 at index 0, 5 at index 2)
expected7 = True
result7 = find_pair(list7, sum7)
print(
    f"Test Case 7: find_pair({list7}, {sum7}) = {result7} (Expected: {expected7}) -> {'PASS' if result7 == expected7 else 'FAIL'}")

# Test Case 8: "Two different elements" - no other instance of X exists
# Here, lst[0] (which is 5) needs a complement of 5.
# exist(lst[1:], 5) will be called, but 5 is not in [10, 20]. So it should be False.
list8 = [5, 10, 20]
sum8 = 10  # Needs (5, 5), but only one 5 exists
expected8 = False
result8 = find_pair(list8, sum8)
print(
    f"Test Case 8: find_pair({list8}, {sum8}) = {result8} (Expected: {expected8}) -> {'PASS' if result8 == expected8 else 'FAIL'}")

# Test Case 9: Pair at the end of the list
list9 = [1, 2, 3, 4, 5, 6]
sum9 = 11  # (5, 6)
expected9 = True
result9 = find_pair(list9, sum9)
print(
    f"Test Case 9: find_pair({list9}, {sum9}) = {result9} (Expected: {expected9}) -> {'PASS' if result9 == expected9 else 'FAIL'}")

# Test Case 10: Larger list, sum in middle
list10 = list(range(1, 21))  # [1, 2, ..., 20]
sum10 = 25  # e.g., (5, 20), (10, 15), etc.
expected10 = True
result10 = find_pair(list10, sum10)
print(
    f"Test Case 10: find_pair({list10[:5]}...{list10[-5:]}, {sum10}) = {result10} (Expected: {expected10}) -> {'PASS' if result10 == expected10 else 'FAIL'}")

# Test Case 11: Larger list, no sum
list11 = list(range(1, 21))
sum11 = 100  # Too large
expected11 = False
result11 = find_pair(list11, sum11)
print(
    f"Test Case 11: find_pair({list11[:5]}...{list11[-5:]}, {sum11}) = {result11} (Expected: {expected11}) -> {'PASS' if result11 == expected11 else 'FAIL'}")