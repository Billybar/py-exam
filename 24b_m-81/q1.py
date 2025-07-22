# --- AI ---

def biggest_sum(lst):
    zero_indices = []
    # Find all indices where 0 appears
    for i in range(len(lst)):
        if lst[i] == 0:
            zero_indices.append(i)

    # Initialize with a value lower than any possible sum (sums are non-negative)
    max_segment_sum = -1

    # Iterate through consecutive pairs of zero indices
    for i in range(len(zero_indices) - 1):
        start_zero_idx = zero_indices[i]
        end_zero_idx = zero_indices[i+1]

        current_segment_sum = 0
        # Sum the numbers strictly between the two zeros
        for j in range(start_zero_idx + 1, end_zero_idx):
            current_segment_sum += lst[j]

        # Update the maximum sum if the current segment's sum is greater
        if current_segment_sum > max_segment_sum:
            max_segment_sum = current_segment_sum

    return max_segment_sum


# --- Question 1, Section B: biggest_sum_row ---

def biggest_sum_row(mat):
    max_overall_sum = -1  # Initialize with a value lower than any possible sum
    row_with_max_sum_index = -1

    # Iterate through each row with its index
    for i in range(len(mat)):
        current_row = mat[i]
        # Use the biggest_sum function to get the max sum for the current row
        current_row_max_sum = biggest_sum(current_row)

        # Update overall max sum and corresponding row index
        if current_row_max_sum > max_overall_sum:
            max_overall_sum = current_row_max_sum
            row_with_max_sum_index = i

    return row_with_max_sum_index