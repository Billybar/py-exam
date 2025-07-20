FIRST_INDEX = 0
SECOND_INDEX = 1

def find_max(lst):
    """
        Find the maximum value in a sorted and possibly rotated list.
        Args:
            lst: A list of integers that was initially sorted and may have been rotated
        Returns:
            The maximum value in the list or None if the list is empty
        """
    # Handle edge cases
    if not lst:
        return None
    if len(lst) == 1:
        return lst[FIRST_INDEX] # max val

    # init indexes
    left = FIRST_INDEX
    right = len(lst) - 1

    # Binary search to find the rotation point (which will be the maximum)
    while left <= right:
        mid = (left + right) // 2  # integer overflow?

        # Check if mid is the pivot point (maximum)
        if mid < len(lst) - 1 and lst[mid] > lst[mid + 1]:
            return lst[mid] # max val

        if mid > 0 and lst[mid - 1] > lst[mid]:
            return lst[mid - 1] # max val

        if lst[right] > lst[left] and lst[right] > lst[mid]:
            return lst[right] # max val

        # max val is on the right side
        if lst[mid] > lst[left]:
            left = mid + 1

        # max val is on the left side
        elif lst[mid] < lst[left]:
            right = mid - 1

    return None # shouldest get to this point

## =========================================
## Q2
def find_pairs(lst, k):
    """ Find the number of pairs in the list where the difference equals k.
        Args:
            lst: A list of integers, sorted in ascending order
            k: The target difference between elements
        Returns:
            int: Total number of pairs with difference equal to k """
    total_pairs = 0
    left = FIRST_INDEX
    right = SECOND_INDEX
    # Small epsilon for floating point comparison
    epsilon = 1e-9

    # Edge case: a list with fewer than 2 elements cannot form pairs
    if len(lst) < 2:
        return total_pairs

    while right < len(lst):

        # If both pointers are at the same position, move right pointer
        if left == right:
            right += 1
            if right == len(lst):
                break

        diff = lst[right] - lst[left]

        if abs(diff - k) < epsilon:
            total_pairs += 1
            # Move both pointers to find the next pair
            left += 1
            right += 1

        elif diff < k:
            # Need a larger difference, move right pointer
            right += 1

        else: # diff > k
            # Need a smaller difference, move left pointer
            left +=1

    return total_pairs

### ===========================================
## Q3.a
def update_list(lst, value):
    """ Update a list by removing the first occurrence of a value.
        Args:lst: The list to be updated
            value: The value to remove from the list
        Returns:The updated list after removing the value (if found) """
    return remove_value(lst, value, FIRST_INDEX)

def remove_value(lst, val,i):
    """
        Helper function that recursively searches for a value to remove.
        Args:
            lst: The list to search through
            val: The value to find and remove
            i: Current index position in the list
        Returns:
            The list after potentially removing the value
        """
    # if scanned the all list and value not found -> return original list
    if i == len(lst):
        return lst

    # if match -> delete and return list
    if val == lst[i]:
        del lst[i]
        return lst

    # value not found yet -> move to the next element
    return remove_value(lst, val, i + 1)


## ===========================================
## Q3.b
def equal_lists(lst1,lst2):
    """
        Check if two lists contain the same elements (potentially in different order).
        This function works by removing elements from both lists recursively.
        Args:
            lst1: First list to compare
            lst2: Second list to compare
        Returns:
            Boolean indicating whether the lists contain the same elements
        """

    # if not the same length ( its mean lst1 wasn't updated because value from lst2 wasn't in lst1 )
    if len(lst1) != len(lst2):
        return False

    # if lists the same
    if lst1 == lst2:
        return True

    # pop last element from lst2 and check if element in lst1
    val = lst2.pop()
    update_list(lst1, val)

    return equal_lists(lst1,lst2)


## ===========================================
## Q4
def is_palindrome(lst):
    # empty list
    if not lst:
        return True

    if is_list_palindrome(lst):
        return True
    else:
        return False


def is_list_palindrome(lst,left_index = FIRST_INDEX , right_index = None):
    # Initialize right index on first call only
    if right_index is None:
        right_index = len(lst) -1

    # if left ptr > right ptr -> True
    if left_index > right_index:
        return True

    # if words not the sames -> False
    if lst[left_index] != lst[right_index]:
        return False

    # if words not palindrome -> False
    if not is_word_palindrome(lst[left_index]):
        return False

    return is_list_palindrome(lst,left_index +1, right_index-1)


def is_word_palindrome(word, left = FIRST_INDEX, right = None):
    # Initialize right index on first call only
    if right is None:
        right = len(word) -1

    # if word empty
    if not word:
        return True

    # if pointers points the same char (middle char) -> True
    if right == left:
        return True

    # if left pointer > right pointer -> True
    if left > right:
        return True

    # if chars not equal -> False
    if word[left] != word[right]:
        return False

    # right ptr > left ptr  -> move to the next chars
    return is_word_palindrome(word, left +1, right -1)