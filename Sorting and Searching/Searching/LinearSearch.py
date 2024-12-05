def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


arr = [1, 12, 9, 5, 6, 10]
key = int(input("Enter the number you want to search: "))
result = linearSearch(arr, key)
if result == -1:
    print("Number not found!!")
else:
    print(f"Number found at index {result}")