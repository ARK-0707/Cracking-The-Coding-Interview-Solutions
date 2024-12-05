def QuickSort(arr, low, high):
    if low < high:
        pivotIndex = Partition(arr, low, high)
        QuickSort(arr, low, pivotIndex - 1)
        QuickSort(arr, pivotIndex + 1, high)


def Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(arr)

size = len(arr)

QuickSort(arr, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(arr)
