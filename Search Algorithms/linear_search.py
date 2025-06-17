def linear_search(arr, target_value):
    for i in range(len(arr)):
        if arr[i] == target_value:
            return i
        
    return -1

arr = [34, 21, 23, 43, 10, 2, 3, 6, 8, 89, 34]
target_value = 43

result = linear_search(arr, target_value)

if result != -1:
    print(f"{target_value} found at index {result}.")

else:
    print(f"{target_value} not found.")