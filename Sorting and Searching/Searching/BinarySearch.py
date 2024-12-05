def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 5, 6, 9, 10, 12]
key = int(input("Enter the number you want to search: "))
result = binarySearch(arr, key)
if result == -1:
    print("Number not found!!")
else:
    print(f"Number found at index {result}")