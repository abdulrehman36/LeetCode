# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return low

array = [3, 4, 5, 6, 9, 10, 11]
x = 7

result = binarySearch(array, x, 0, len(array)-1)

print(result)

