def dist(lst, num):
    if not lst:
        return -1

    n = len(lst)
    first_occurrence_from_left = -1
    last_occurrence_from_right = -1

    # Find the first occurrence from the left
    for i in range(n):
        if lst[i] == num:
            first_occurrence_from_left = i
            break

    if first_occurrence_from_left == -1:
        return -1  # num not found in the list

    # Find the first occurrence from the right
    # (which is the last occurrence overall)
    for i in range(n - 1, -1, -1):
        if lst[i] == num:
            last_occurrence_from_right = n - 1 - i
            break

    return first_occurrence_from_left + last_occurrence_from_right


def min_dist(lst):
    if not lst:
        return None

    min_distance = float('inf')
    num_with_min_dist = None

    # Use a set to avoid re-calculating distance for duplicate numbers
    unique_numbers = []
    seen = set()
    for x in lst:
        if x not in seen:
            unique_numbers.append(x)
            seen.add(x)

    for num in unique_numbers:
        current_dist = dist(lst, num)
        # Only consider valid distances (not -1 for numbers not found,
        # though all unique_numbers will be found)
        if current_dist != -1 and current_dist < min_distance:
            min_distance = current_dist
            num_with_min_dist = num

    return num_with_min_dist


# Test Cases for dist function
print("--- Testing dist function ---")
list1 = [4, 10, 13, 71, 10, 71, 10, 71, 2, 10]
print(f"List: {list1}")
print(f"Distance of 71: {dist(list1, 71)} (Expected: 5)")  # [cite: 24]
print(f"Distance of 13: {dist(list1, 13)} (Expected: 9)")  #
print(f"Distance of 4: {dist(list1, 4)} (Expected: 9)")  # 0 (left) + (10-1-0)=9 (right) = 9
print(f"Distance of 10: {dist(list1, 10)} (Expected: 9)")  # 1 (left) + (10-1-9)=0 (right) = 1
print(f"Distance of 2: {dist(list1, 2)} (Expected: 9)")  # 8 (left) + (10-1-8)=1 (right) = 9
print(f"Distance of 99 (not in list): {dist(list1, 99)} (Expected: -1)")

list2 = [1, 2, 3, 4, 5]
print(f"\nList: {list2}")
print(f"Distance of 1: {dist(list2, 1)} (Expected: 4)")  # 0 + (5-1-0) = 4
print(f"Distance of 3: {dist(list2, 3)} (Expected: 4)")  # 2 + (5-1-2) = 4
print(f"Distance of 5: {dist(list2, 5)} (Expected: 4)")  # 4 + (5-1-4) = 4

list3 = [5, 5, 5, 5]
print(f"\nList: {list3}")
print(f"Distance of 5: {dist(list3, 5)} (Expected: 3)")  # 0 + (4-1-3) = 3

list4 = [10, 20]
print(f"\nList: {list4}")
print(f"Distance of 10: {dist(list4, 10)} (Expected: 1)")  # 0 + (2-1-1) = 1
print(f"Distance of 20: {dist(list4, 20)} (Expected: 1)")  # 1 + (2-1-0) = 1

list5 = []
print(f"\nList: {list5}")
print(f"Distance of 5: {dist(list5, 5)} (Expected: -1)")

# Test Cases for min_dist function
print("\n--- Testing min_dist function ---")
list_min_dist_example = [10, 2, 71, 10, 71, 4, 10, 13, 71, 10]
print(f"List: {list_min_dist_example}")
print(f"Number with min distance: {min_dist(list_min_dist_example)} (Expected: 10)")  #

list6 = [1, 2, 3, 4, 5]
print(f"\nList: {list6}")
print(
    f"Number with min distance: {min_dist(list6)} (Expected: 1, 2, 3, 4 or 5 all have distance 4)")  # All have distance 4. Any can be returned.

list7 = [10, 10, 20, 20]
print(f"\nList: {list7}")
print(f"Distance of 10: {dist(list7, 10)} (0 + (4-1-1) = 2)")
print(f"Distance of 20: {dist(list7, 20)} (2 + (4-1-3) = 2)")
print(f"Number with min distance: {min_dist(list7)} (Expected: 10 or 20, both have distance 2)")

list8 = [
    100]  # Assuming list contains at least two elements based on other questions but this one doesn't explicitly state.
# However, the problem statement for `is_up_down` states "ניתן להניח כי הרשימה המועברת כפרמטר מאותחלת ומכילה לפחות שני איברים. אין צורך לבדוק זאת." [cite: 15]
# This constraint isn't repeated for Q2. If a list with 1 element is allowed:
# dist([100], 100) -> 0 + (1-1-0) = 0
# min_dist([100]) -> 100
# For safety, I'll test with it.
print(f"\nList: {[100]}")
print(f"Distance of 100: {dist([100], 100)} (Expected: 0)")
print(f"Number with min distance: {min_dist([100])} (Expected: 100)")

list9 = []
print(f"\nList: {list9}")
print(f"Number with min distance: {min_dist(list9)} (Expected: None)")