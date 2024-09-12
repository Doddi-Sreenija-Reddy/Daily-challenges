def merge(arr1, arr2):
    n = len(arr1)
    r = len(arr2)
    i = j = 0
    arr3 = []
    while i < n and j < r:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    while i < n:
        arr3.append(arr1[i])
        i += 1
    while j < r:
        arr3.append(arr2[j])
        j += 1
    print("Merged array:")
    print("First part of merged array:")
    for i in range(len(arr1)):
        print(arr3[i], end=" ")
    print()  
    print("Second part of merged array:")
    for i in range(len(arr1), len(arr3)):
        print(arr3[i], end=" ")
    print()  
arr1 = list(map(int, input("Enter elements of the first array separated by space: ").split()))
arr2 = list(map(int, input("Enter elements of the second array separated by space: ").split()))
merge(arr1, arr2)
