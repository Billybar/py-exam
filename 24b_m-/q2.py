import unittest

def find_median(lst, m):
    med = lst[0]
    min_of_max_heap = max(lst[1],lst[2])
    max_of_min_heap = min(lst[1], lst[2])
    med , min_of_max_heap, max_of_min_heap =  get_med_min_max(med,min_of_max_heap,max_of_min_heap)

    i = 3
    # check 2 elements at a time
    while i < len(lst)-1:
        first_val = lst[i]
        second_val = lst[i+1]

        # if both elements above med
        if first_val > med and second_val > med:
            max_of_min_heap = med
            med = max(min_of_max_heap,first_val,second_val)
            min_of_max_heap = get_max_med(first_val,second_val, min_of_max_heap, med)
            i +=2

        # if both elements lower med
        elif first_val < med and second_val < med:
            min_of_max_heap = med
            med = max(max_of_min_heap,first_val,second_val)
            max_of_min_heap = get_min_med(first_val,second_val, max_of_min_heap, med)
            i +=2

        else:
            i +=2
            # first_val > med and second_val < med  OR  first_val < med and second_val > med
            # so min-heaps and max-heap are equal -> med = med

    return med



# helper 1
def get_med_min_max(med,min_of_max_heap,max_of_min_heap):
    if med > min_of_max_heap:
        temp = med
        med = min_of_max_heap
        min_of_max_heap = temp

    # swap if need
    elif max_of_min_heap > med:
        temp = med
        med = max_of_min_heap
        max_of_min_heap = temp

    return med, min_of_max_heap, max_of_min_heap

# helper for nim_med
def get_min_med(first,second, min_med, med):
    if med == first:
        min_med = max(min_med,second)
    elif med == second:
        min_med = max(min_med,first)
    else: # med == min_med
        min_med = max(first,second)
    return min_med

# helper for max_med
def get_max_med(first,second, max_med, med):
    if med == first:
        max_med = min(max_med,second)
    elif med == second:
        max_med = min(max_med,first)
    else: # med == max_med
        max_med = min(first,second)
    return max_med

# --- Test Cases ---

def run_tests():
    print("Running tests for find_median function...")

    # Test Case 1: Example from problem description
    lst1 = [11, 6, 8, 7, 3, 4, 1]
    m1 = 11
    expected1 = 6
    result1 = find_median(lst1, m1)
    print(f"Test 1: lst={lst1}, m={m1}")
    print(f"  Expected: {expected1}, Actual: {result1}")
    assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"
    print("  Test 1 Passed.")

    # Test Case 2: Smallest list (n=3)
    lst2 = [5, 1, 9]
    m2 = 10
    expected2 = 5
    result2 = find_median(lst2, m2)
    print(f"Test 2: lst={lst2}, m={m2}")
    print(f"  Expected: {expected2}, Actual: {result2}")
    assert result2 == expected2, f"Test 2 Failed: Expected {expected2}, got {result2}"
    print("  Test 2 Passed.")

    # Test Case 3: Larger list, median in the middle (this test failed in your unittest run)
    lst3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    m3 = 100
    expected3 = 50
    result3 = find_median(lst3, m3)
    print(f"Test 3: lst={lst3}, m={m3}")
    print(f"  Expected: {expected3}, Actual: {result3}")
    assert result3 == expected3, f"Test 3 Failed: Expected {expected3}, got {result3}"
    print("  Test 3 Passed.")

    # Test Case 4: List with values closer to 0
    lst4 = [0, 1, 2, 3, 4]
    m4 = 4
    expected4 = 2
    result4 = find_median(lst4, m4)
    print(f"Test 4: lst={lst4}, m={m4}")
    print(f"  Expected: {expected4}, Actual: {result4}")
    assert result4 == expected4, f"Test 4 Failed: Expected {expected4}, got {result4}"
    print("  Test 4 Passed.")

    # Test Case 5: List with values closer to m
    lst5 = [95, 96, 97, 98, 99]
    m5 = 100
    expected5 = 97
    result5 = find_median(lst5, m5)
    print(f"Test 5: lst={lst5}, m={m5}")
    print(f"  Expected: {expected5}, Actual: {result5}")
    assert result5 == expected5, f"Test 5 Failed: Expected {expected5}, got {result5}"
    print("  Test 5 Passed.")

    # Test Case 6: Unsorted list, larger values (this test failed in your unittest run)
    lst6 = [500, 100, 300, 700, 200, 600, 400]
    m6 = 700
    expected6 = 400
    result6 = find_median(lst6, m6)
    print(f"Test 6: lst={lst6}, m={m6}")
    print(f"  Expected: {expected6}, Actual: {result6}")
    assert result6 == expected6, f"Test 6 Failed: Expected {expected6}, got {result6}"
    print("  Test 6 Passed.")


    print("\nAll tests completed.")

if __name__ == '__main__':
    run_tests()
