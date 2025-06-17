def binary_search(arr, target_value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target_value:
            return mid
        
        if arr[mid] > target_value:
            right = mid - 1

        else:
            left = mid + 1

    return -1

arr = [2, 4, 5, 6, 7, 8, 9, 11, 15, 17, 30, 32, 45]
target_value = 30

result = binary_search(arr, target_value)

if result != -1:
    print("value", target_value, "found at index", result)

else:
    print("Target value not found in the array")

            