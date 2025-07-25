def long_sub_lst(lst):
    current_seq , max_seq = 1,1
    prev = 0

    for i in range(1,len(lst)):
        current = lst[i]
        prev = lst[i-1]

        if current > 0 > prev:
            current_seq += 1
        elif current < 0 < prev:
            current_seq += 1
        else:
            current_seq = 1

        if current_seq > max_seq:
            max_seq = current_seq

    return max_seq