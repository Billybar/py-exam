def two_sum(self, lst, target):
    # Time Complexity: O(n) - We iterate through the list once.
    # Create a dictionary to store numbers and their indices
    num_map = {}

    # Iterate through the array with both index and value
    for i, num in enumerate(lst):
        # Calculate the complement needed
        complement = target - num

        # Check if the complement is already in our map
        if complement in num_map:
            # If found, we have our two numbers. Return their indices.
            # The problem states to return the smaller index first,
            # which is naturally handled by this approach since num_map[complement] 
            # would have been added earlier (smaller index) than the current 'i'.
            return [num_map[complement], i]

        # If not found, add the current number and its index to the map
        num_map[num] = i

    # This part should ideally not be reached if the problem guarantees a solution.
    # It's good practice for robust code, but for this specific problem,
    # it implies no solution was found.
    return []


#### - 2 pass solution
def two_suum(self, lst, target):
    # Time Complexity: O(n) - Due to two passes over the list, each taking O(n) time.
    # Space Complexity: O(n) - For storing elements in the hash map.

    # Initialize a hash map to store numbers and their indices.
    # Key: number, Value: its index in the 'nums' list.
    indices = {} # val -> index

    # First pass: Populate the hash map with all numbers and their indices.
    # If duplicate numbers exist, this stores the index of the last occurrence.
    for i, n in enumerate(lst):
        indices[n] = i

    # Second pass: Find the complement for each number.
    for i, n in enumerate(lst):
        diff = target - n  # Calculate the required complement

        # Check if the complement exists in the map AND
        # ensure it's not the current number itself (i.e., different indices).
        if diff in indices and indices[diff] != i:
            # Return the indices of the current number and its complement.
            # The problem asks for the smaller index first. This approach
            # might return [larger_index, smaller_index] in some cases.
            # For strict adherence, one might use `sorted([i, indices[diff]])`.
            return [i, indices[diff]]

    # This part should ideally not be reached as the problem guarantees a solution.
    return []