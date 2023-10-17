
t = int(input())
while t > 0:
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    tot = 0
    for i in range(n):
        tot += arr[i] // k
        arr[i] %= k
    arr.sort()
    l = 0
    r = n - 1
    while l < r:
        if arr[l] + arr[r] >= k:
            tot += 1
            l += 1
            r -= 1
        else:
            l += 1
    print(tot)
    t -= 1
