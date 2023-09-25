t = int(input())
while t > 0:

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    l = 0
    pre = [0 for _ in range(n + 1)]
    for i in range(n):
        pre[i + 1] = pre[i] + a[i]
    res = 0

    for i in range(n):

        while l <= i and pre[i + 1] - pre[l] > k:
            l += 1
        if l <= i and i > 0 and h[i - 1] % h[i] != 0:
            l = i
        res = max(res, i - l + 1)

    print(res)

    t -= 1
