def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

array = [2, 4, 5, 6, 7, 8, 9, 11, 15, 17, 30, 32, 45]
targ = 11
result = binary_search(array, targ)

if result != -1:
    print(f"Value {targ} found at index {result}")
else:
    print("Target value not found in the array")


## This algorithm uses O(logn) time complexity --> the size of input reduces by 50% in every run
