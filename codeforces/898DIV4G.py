t = int(input())
while t > 0:
    s = input()
    n = len(s)
    cnt = 0
    ### 向左边匹配
    al = (s[0] == "B" or s[n - 1] == "B")
    for i in range(n - 1):
        if s[i] == s[i + 1] and s[i] == "B":
            al = True
    ans = []
    cur = 0
    for i in range(n):
        if s[i] == "A":
            cur += 1
        else:
            if cur > 0:
                ans.append(cur)
            cur = 0
    if cur > 0:
        ans.append(cur)
    res = 0
    ans.sort()
    if al and len(ans) > 0:
        res += ans[0]
    for i in range(1, len(ans)):
        res += ans[i]

    print(res)

    t -= 1
