def minus_plus(lst):
    return is_minus_plus_lst(lst, 0)

def is_minus_plus_lst(lst,index):
    # if visited all numbers -> True
    if index == len(lst):
        return True

    if not is_num_have_twin(lst, lst[index], 0 ):
        return False

    # go to next number
    return is_minus_plus_lst(lst, index+1)

def is_num_have_twin(lst, num, index):
    if index == len(lst):
        return False

    # if there is a twin - > True
    if lst[index] == -num:
        return True

    return is_num_have_twin(lst, num, index+1)
