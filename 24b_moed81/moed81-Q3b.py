def is_palindrome(lst):
    return is_list_palindrome(lst,0,len(lst)-1)


def is_list_palindrome(lst, right,left):
    # if visit each word -> True
    if right > left:
        return True

    # if symmetric words not the same -> False
    if lst[right] != lst[left]:
        return False

    # check one of the words
    word = lst[right]
    if not is_word_palindrome(word,0,len(word)-1):
        return False
    return is_list_palindrome(lst, right+1, left-1)


def is_word_palindrome(word, right,left):
    # break condition
    if right >= left:
        return True

    if word[right] != word[left]:
        return False

    return is_word_palindrome(word, right+1, left-1)


