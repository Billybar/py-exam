# 3sum style
import unittest


def count_triples(lst, target):
    triplets_counter = 0

    for i in range(len(lst)-2):

        left, right = i+1, len(lst) -1
        while left < right:
            sum = lst[i] * lst[left] * lst[right]

            if sum == target:
                triplets_counter +=1
                left +=1
                right -=1

            elif sum < target:
                left += 1

            else:  # sum > target
                right -= 1

    return triplets_counter