def missing_number(arr):
    n = len(arr)
    j = 1
    c = 0
    for i in range(0,n):
        if j == arr[i]:
            j=j+1
        else:
            c = i+1
            i = i-1
            print("Missing number: ",c)
            break
    if c==0:
        print("Missing number: ",n+1)
    
arr = list(map(int, input("Enter the array: ").split()))
missing_number(arr)
