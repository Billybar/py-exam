def union(lst1, lst2):
    uni = []
    ptr1, ptr2 = 0,0

    while ptr1 < len(lst1) and ptr2 < len(lst2):
        vala = lst1[ptr1]
        valb = lst2[ptr2]
        if vala == valb:
            ptr1 += 1
            ptr2 += 1
            uni.append(vala)

        elif vala < valb:
            uni.append(vala)
            ptr1 +=1

        elif valb < vala:
            uni.append(valb)
            ptr2 += 1

    # Add remaining elements from lst1, if any
    while ptr1 < len(lst1):
        uni.append(lst1[ptr1])
        ptr1 += 1

    # Add remaining elements from lst2, if any
    while ptr2 < len(lst2):
        uni.append(lst2[ptr2])
        ptr2 += 1

    return uni


print("--- Test Cases ---")

# Test Case 1: Basic merge with no common elements
list1_1 = [1, 3, 5]
list1_2 = [2, 4, 6]
expected1 = [1, 2, 3, 4, 5, 6]
result1 = union(list1_1, list1_2)
print(f"Test Case 1: {list1_1} U {list1_2} = {result1} (Expected: {expected1}) -> {'PASS' if result1 == expected1 else 'FAIL'}")

# Test Case 2: Lists with common elements
list2_1 = [1, 2, 3, 4]
list2_2 = [3, 4, 5, 6]
expected2 = [1, 2, 3, 4, 5, 6]
result2 = union(list2_1, list2_2)
print(f"Test Case 2: {list2_1} U {list2_2} = {result2} (Expected: {expected2}) -> {'PASS' if result2 == expected2 else 'FAIL'}")

# Test Case 3: One list is empty
list3_1 = []
list3_2 = [10, 20, 30]
expected3 = [10, 20, 30]
result3 = union(list3_1, list3_2)
print(f"Test Case 3: {list3_1} U {list3_2} = {result3} (Expected: {expected3}) -> {'PASS' if result3 == expected3 else 'FAIL'}")

# Test Case 4: Both lists are empty
list4_1 = []
list4_2 = []
expected4 = []
result4 = union(list4_1, list4_2)
print(f"Test Case 4: {list4_1} U {list4_2} = {result4} (Expected: {expected4}) -> {'PASS' if result4 == expected4 else 'FAIL'}")

# Test Case 5: Elements remaining in list1 after loop
list5_1 = [1, 2, 7, 8]
list5_2 = [3, 4, 5]
expected5 = [1, 2, 3, 4, 5, 7, 8]
result5 = union(list5_1, list5_2)
print(f"Test Case 5: {list5_1} U {list5_2} = {result5} (Expected: {expected5}) -> {'PASS' if result5 == expected5 else 'FAIL'}")

# Test Case 6: Elements remaining in list2 after loop
list6_1 = [1, 2, 3]
list6_2 = [4, 5, 6, 7, 8]
expected6 = [1, 2, 3, 4, 5, 6, 7, 8]
result6 = union(list6_1, list6_2)
print(f"Test Case 6: {list6_1} U {list6_2} = {result6} (Expected: {expected6}) -> {'PASS' if result6 == expected6 else 'FAIL'}")

# Test Case 7: Lists with negative numbers
list7_1 = [-5, -2, 0]
list7_2 = [-3, -1, 1]
expected7 = [-5, -3, -2, -1, 0, 1]
result7 = union(list7_1, list7_2)
print(f"Test Case 7: {list7_1} U {list7_2} = {result7} (Expected: {expected7}) -> {'PASS' if result7 == expected7 else 'FAIL'}")

# Test Case 8: Lists with duplicate elements within themselves (input lists are strictly sorted)
# The problem statement specified "ממויינות בסדר עולה ממש" (strictly ascending order),
# so internal duplicates in the input lists are not expected based on the prompt.
# However, if 'strictly' meant the output should only have unique elements and inputs *could* have duplicates,
# the interpretation would change. Assuming input lists are truly unique and sorted.
list8_1 = [1, 3, 5, 7]
list8_2 = [1, 3, 5, 7]
expected8 = [1, 3, 5, 7] # Union of two identical sets
result8 = union(list8_1, list8_2)
print(f"Test Case 8: {list8_1} U {list8_2} = {result8} (Expected: {expected8}) -> {'PASS' if result8 == expected8 else 'FAIL'}")