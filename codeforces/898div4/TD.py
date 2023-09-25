t = int(input())
while t > 0:
    n, k = map(int, input().split())
    s = input()
    i = 0
    cnt = 0
    while i < n:
        while i < n and s[i] != "B":
            i += 1
        if i < n and s[i] == "B":
           cnt += 1
        i += k
    print(cnt)
    t -= 1