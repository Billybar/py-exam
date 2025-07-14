def complement(lst):
    if not lst:
        return []

    max_val  = max(lst)

    # Create a boolean array (or list of 0s and 1s as implied in the solution)
    # to mark the presence of numbers from 1 to max_val.
    # The size is max_val + 1 because we care about values up to max_val,
    # and we'll use 1-based indexing for the numbers themselves.
    present_numbers = [0] * (max_val + 1)

    for val in lst:
        # Mark the number as present
        present_numbers[val] = 1    # The provided solution uses +=1, but 1 is sufficient to mark presence.

    final_list = []
    for i in range(1, max_val + 1): # Iterate from 1 to max_val inclusive
        if present_numbers[i] == 0: # If the number is not marked as present
            final_list.append(i)    # Add it to the complement list

    return final_list