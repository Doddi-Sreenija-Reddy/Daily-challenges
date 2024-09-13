def leader(arr):
    n = len(arr)
    i = j = c = 0
    for i in range(0,n):
        for j in range(i+1,n):  
            if arr[i]<=arr[j]:
                c = 0
                break 
            else:
                c = arr[i]
        if (c>0) and (i<n-1):
            print(c)
    print(arr[n-1])
arr = list(map(int, input().split()))
leader(arr)
