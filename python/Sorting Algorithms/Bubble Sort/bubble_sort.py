def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        swappped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[i], arr[j+1] = arr[j+1], arr[i]
                swappped = True

        if not swappped:
            break

    return arr

arr = [3, 4, 6, 7, 4, 3, 2, 56, 7, 5, 343, 2, 32, 2]
print("Sorted array:", bubble_sort(arr))

        
        