# 2sum sorted
def tow_sum(lst, target):
    left, right = 0, len(lst) -1

    while left < right:
        sum = lst[left] + lst[right]

        if sum == target:
            return [left, right]

        elif sum < target:
            left += 1

        else: # sum > target
            right -= 1

    return []