def common(lst1,lst2):
    common_lst = []
    i = j = 0
    while i != len(lst1) and j != len(lst2):
        a = lst1[i]
        b = lst2[j]

        if a < b:
            i += 1
        elif b < a:
            j += 1
        elif a == b:
            common_lst.append(a)
            i += 1
            j += 1

    if not common_lst:
        return None
    return common_lst


def main():
    lst1 = [-4, 0, 2, 3, 8, 9]
    lst2 = [-4, -2, 1, 3, 5, 10, 12]
    print(common(lst1, lst2))

    lst1 = [-4, 0, 2, 3, 8, 9]
    lst2 = [1, 4, 5, 10, 12]
    print(common(lst1, lst2))


if __name__ == "__main__":
    main()