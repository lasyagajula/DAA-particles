def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


arr = [25, 10, 30, 5, 15, 20]

print("Original Array:", arr)
print("Sorted Array:", quicksort(arr))
