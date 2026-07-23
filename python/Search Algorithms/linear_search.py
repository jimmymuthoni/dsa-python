def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

array = [23,14,54,32,12,67,8,8]
target = 12
result = linear_search(array, target)
if result != -1:
    print(f"Value {target} found at index {result}")

else:
    print("Target value not found.")

"""
This algoritm runs with O(n) --> Worst case scenario we can go through
the entire array before getting the target value
"""