def  max_pos_seq(lst):
    return _find_max(lst,0)

def _find_max(lst, index):
    if index >= len(lst):
        return 0

    current_length = _count_sequence(lst, index)
    next_index = index + max(1, current_length)
    longest_seq = _find_max(lst, next_index)

    return max(current_length, longest_seq)

# basic sum recursive
def _count_sequence(lst, index):
    if index >= len(lst) or lst[index] < 0:
        return 0
    return 1 + _count_sequence(lst,index + 1) # 1 + next call