def max_drop(lst):
        # Initialize max_so_far with the first element of the list.
        # This variable will keep track of the maximum value encountered so far
        # as we iterate through the list from left to right.
    max_so_far = lst[0]

    # Initialize max_difference to 0. This will store the largest drop found.
    # A drop is defined as max_so_far - current_element.
    max_difference = 0

    # Variables to store the actual elements that result in the max_difference.
    # These are initialized to None or default values.
    high_val_for_max_drop = None
    low_val_for_max_drop = None

    # Iterate through the list starting from the first element.
    # We compare each element with the maximum element found *before or at* its position.
    for i in range(len(lst)):
        current_element = lst[i]

        # If the current element is greater than max_so_far,
        # it means we have found a new potential peak.
        # We update max_so_far to this new peak, as it could be the start
        # of a new maximum drop.
        if current_element > max_so_far:
            max_so_far = current_element
        else:
            # If the current element is not greater than max_so_far,
            # it means there's a possibility of a drop (current_element < max_so_far).
            # Calculate the potential drop (difference).
            current_drop = max_so_far - current_element

            # If this current_drop is greater than the max_difference found so far,
            # update max_difference and store the corresponding high and low values.
            if current_drop > max_difference:
                max_difference = current_drop
                high_val_for_max_drop = max_so_far
                low_val_for_max_drop = current_element

    # Print the elements that resulted in the maximum drop, as required by the problem.
    # This check ensures that we only print if a drop was actually found (max_difference > 0).
    if max_difference > 0:
        print(f"The elements are {int(high_val_for_max_drop)}, {int(low_val_for_max_drop)} and the returned value is {int(max_difference)}")
    else:
        # If no drop was found (e.g., list is sorted in strictly ascending order),
        # the problem implies returning 0. We print a message for clarity.
        print("No suitable drop found.")

    return max_difference
