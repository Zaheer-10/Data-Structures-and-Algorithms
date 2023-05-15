def binary_search(array, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, low, mid - 1, target)
    else:
        return binary_search(array, mid + 1, high, target)

array = [1, 2, 3, 4, 5, 6, 7, 8, 13, 55, 89, 114]
bs = binary_search(array, 0, len(array) - 1, 89)
if bs == -1:
    print("Oops! Element not found.")
else:
    print("Element found at position:", bs)
