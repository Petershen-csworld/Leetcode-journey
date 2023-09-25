from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    g = defaultdict(int)
    for ch in s:
        g[ch] += 1


    def check(num):
        cnt = 0
        tot = 0
        for key, number in g.items():
            if number % 2 == 1:
                cnt += 1
            tot += number
        ### at least length num
        ### if num is even
        ##for every alphabet with even chars
        ## we need a string to consume the even items
        ### if num is odd
        ### we wanna as many odd ones as possible to reduce the length
        ### we can divide the even numbers into several odd ones


        if num % 2 == 0:
            return cnt * (num + 1) + (k - cnt) * num <= tot
        else:
            if k % 2 == 0:
                ### if k is even
                ### we can request odd from even ones
                return num * k <= tot
            else:
                return num * (k - 1) + num + 1 <= tot

    ans = 1
    l = 1
    r = n // k

    while l < r:
        mid = l + r + 1 >> 1
        if check(mid):
            l = mid
            ans = max(ans, mid)
        else:
            r = mid - 1
    print(ans)
