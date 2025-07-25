def long_sub_lst(lst):
    count , max_lan, prev = 0,0,0

    for i in range(len(lst)):
        current = lst[i]
        if i > 0:
            prev = lst[i-1]

        if current > 0 and prev < 0:
            count += 1
        elif current < 0 and prev  > 0:
            count += 1
        else:
            count = 1

        if count > max_lan:
            max_lan = count

    return max_lan