t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(key = lambda x: -x)
    used = [False for _ in range(n + 1)]
    ok = True
    for i in range(n):
        x = a[i]
        while x > n or used[x]:
            x = x // 2
        if x > 0:
            used[x] = True
        else:
            ok = True
    print("YES") if ok else print("NO")

    t -= 1