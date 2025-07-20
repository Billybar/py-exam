############################
## --------- Q1 --------- ##
def complement(lst):
    """
        Find the complement list of a given list of natural numbers.

        Args:
            lst (list): A list of natural numbers.

        Returns:
            list: The complement list. If the input list is empty or contains all
                  numbers from 1 to its maximum value, an empty list is returned.
        """
    if not lst:
        return []
    
    lst_complement = []
    lst_copy = lst.copy()

    # loop list and exctrat the top 2 max each time
    while lst_copy:
        max_val = max(lst_copy)
        lst_copy.remove(max_val)

        # validate list not empty
        if len(lst_copy) > 0:
            second_max_val = max(lst_copy)
        else:
            second_max_val = 0

        # fill in the gaps between top 2 max vals
        for i in range(second_max_val + 1 , max_val):
            lst_complement.append(i)

    return sorted(lst_complement)





############################
## --------- Q2 --------- ##

## Q2.a
def shift_k_right(lst, k):
    """
        Performs a right circular shift on a list by k positions.

        Args:
            lst: A list of elements to be shifted
            k: A non-negative integer representing the number of positions to shift

        Returns:
            A new list with elements shifted k positions to the right

        Raises:
            ValueError: If k is negative or greater than the length of the list
        """
    if k < 0 or k > len(lst):
        raise ValueError("Invalid value for k")

    if not lst:
        return []

    # incase k == lst length
    k = k % len(lst)

    # return updated list after shift
    return lst[-k:] + lst[:-k]


## Q2.b
def shift_right_size(a,b):
    """
        Determines the size of right shift needed to make list b identical to list a.

        Args:
            a: The target list
            b: The list to be shifted

        Returns:
            An integer representing the number of positions to shift list b right to
            match list a, or None if no such shift exists

        Note:
            Returns None if the lists have different lengths
        """
    # validate
    if len(a) != len(b):
        return None
    if not a and not b:
        return 0

    # check if a == b after each shift
    for shift_size in range(len(a)):
        if a == shift_k_right(b, shift_size):
            return shift_size

    return None





############################
## --------- Q3 --------- ##

FIRST_INDEX = 0

def is_perfect(lst):
    """
        Checks if a list is perfect according to the "scanning by cell values" rule.

        A perfect list is one where:
        1. All cells are visited during scanning
        2. The scanning terminates (by reaching a cell with value 0)

        Scanning starts at index 0 and moves to the index equal to the value of the current cell.

        Args:
            lst: A list of integers

        Returns:
            True if the list is perfect, False otherwise

        Raises:
            IndexError: If an index is out of range
            TypeError: If a list element is not an integer
        """
    if not lst:
        return True

    # Initialize tracking of visited cells
    is_visited = [False] * len(lst)
    current_index = FIRST_INDEX

    # loop maximum list length
    for _ in range(len(lst)):
        is_visited[current_index] = True
        current_index = lst[current_index]

        # if not int
        if not isinstance(current_index, int):
            raise TypeError("value is not int")

        # if index overflow
        if current_index >= len(lst) or current_index < FIRST_INDEX:
            raise IndexError("index overflow")

        # if back to first index -> break
        if current_index == FIRST_INDEX:
            break

    # if not all visited return False
    for visited in is_visited:
        if not visited:
            return False

    # list is perfect
    return True





############################
## --------- Q4 --------- ##

## Q4.A
def identity_matrix(mat):
    """
        Check if a given matrix is an identity matrix.
        Args:
            mat (list): A 2D list representing a matrix

        Returns:
            bool: True if mat is an identity matrix, False otherwise

        Raises:
            TypeError: If any element in the matrix is not an integer
        """
    if not mat:
        return False

    row_size = len(mat)

    # if it's not square -> return False
    for row in mat:
        if len(row) != row_size:
            return False

    # if it's an identity matrix
    for i in range(len(mat)):
        for j in range(len(mat[i])):

            # if not int
            if not isinstance(mat[i][j],int):
                raise TypeError("Not all values are int")

            # val must be 0 unless its diagonal
            if mat[i][j] != 0:
                # if its diagonal and 1 -> continue
                if i == j and mat[i][j] == 1:
                    continue
                return False
    return True


## Q4.b
def create_sub_matrix(mat, size):
    """
        Create a square sub-matrix of specified size from the center of the original matrix.

        Args:
            mat (list): A 2D list representing a square matrix
            size (int): Size of sub-matrix to create (must be odd)

        Returns:
            list: A 2D list representing the sub-matrix

        Raises:
            IndexError: If rows have different lengths
        """
    mat_row_size = len(mat)
    mat_col_size = len(mat[0])

    # Check if all rows have the same length
    for row in mat:
        if len(row) != mat_col_size:
            raise IndexError("Not all rows are equal")

    # check if size valid
    if size > mat_col_size:
        raise ValueError("invalid size")

    # get the offset of sub_mat
    row_offset = (mat_row_size - size) // 2
    col_offset = (mat_col_size - size) // 2

    # Create the sub-matrix
    sub_mat = []
    for i in range(row_offset, row_offset + size):
        sub_row = []
        for j in range(col_offset, col_offset + size):
            sub_row.append(mat[i][j])
        sub_mat.append(sub_row)

    return sub_mat


## Q4.c
def max_identity_matrix(mat):
    """
        Find the maximum size identity matrix centered in the given matrix.

        Args:
            mat (list): A 2D list representing a matrix with odd dimensions

        Returns:
            int: Size of the maximum identity matrix found, or 0 if none exists
        """
    max_size = 0

    # Check all possible odd-sized sub-matrices start from 1
    for size in range(1, len(mat) + 1, 2 ):
        try:
            sub_mat = create_sub_matrix(mat, size)

            # validate sub_mat not empty
            if sub_mat:
                if identity_matrix(sub_mat):
                    max_size = size
                else:
                    # stop looking for bigger matrix
                    break

        except IndexError as e:
            print(f"Error: {e}")
            return 0
        except TypeError as e:
            print(f"Error: {e}")
            return 0
        except ValueError as e:
            print(f"Error: {e}")
            return 0

    return max_size