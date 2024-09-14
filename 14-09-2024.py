def subarray(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            c = 0  
            for k in range(i, j + 1):
                c += arr[k]
            if c == 0:
                print("[", i, ",", j, "]")
arr = list(map(int, input().split()))
subarray(arr)
