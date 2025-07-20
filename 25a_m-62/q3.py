
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
