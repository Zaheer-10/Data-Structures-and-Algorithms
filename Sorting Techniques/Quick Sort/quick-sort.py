def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of the smaller element
    i = low - 1

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            # Swap elements at i and j
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at the partition index
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Find the partitioning index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after the partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
quick_sort(arr, 0, n - 1)

print("Sorted array:")
for i in range(n):
    print(arr[i], end=" ")
