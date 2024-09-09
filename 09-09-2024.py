def dutch_national_flag_sort(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
arr = list(map(int, input("Enter the array elements (0, 1, and 2 only) separated by spaces: ").split()))
dutch_national_flag_sort(arr)
print("Sorted array:", arr)
