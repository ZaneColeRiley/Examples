def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low < high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1


array = [1, 12, 32, 46, 15, 35, 5]
X = 46

if X in array:
    print("Found X at index: {}".format(binary_search(array, X)))
if X not in array:
    print("X is not found.")
