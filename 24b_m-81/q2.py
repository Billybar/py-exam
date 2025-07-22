def common(lst1, lst2):
    common_elements = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            common_elements.append(lst1[i])
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            i += 1
        else:
            j += 1

    if not common_elements:
        return None
    return common_elements