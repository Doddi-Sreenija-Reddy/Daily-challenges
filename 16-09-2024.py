def reverse(arr):
    n = len(arr)
    a = n // 2
    for i in range(a):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i] 
    for i in range(n):
        print(arr[i], end=' ')
s = input()
words = s.split()
reverse(words)
