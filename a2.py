# Function to find the most frequent element
def find_most_frequent(arr):
    most_frequent = 0
    max_count = 0

    # Outer loop to pick each element one by one
    for i in range(len(arr)):
        count = 0
        # Inner loop to count occurrences of the current element
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        # Check if the current element has already been counted before
        already_counted = False
        for k in range(i):
            if arr[i] == arr[k]:
                already_counted = True
                break

        # If the element hasn't been counted, check if it's the most frequent
        if not already_counted and count > max_count:
            max_count = count
            most_frequent = arr[i]

    # If all elements occur only once, return None
    if max_count == 1:
        return None
    else:
        return most_frequent, max_count


# Test cases
arr1 = [5, 6, 7, 5, 6, 7, 5, 8]
arr2 = [1, 2, 3, 4, 5]
arr3 = [9, 9, 9, 9]
arr4 = [2, 3, 4, 5, 6]

print(find_most_frequent(arr1))  # Expected: (5, 3)
print(find_most_frequent(arr2))  # Expected: None
print(find_most_frequent(arr3))  # Expected: (9, 4)
print(find_most_frequent(arr4))  # Expected: None



