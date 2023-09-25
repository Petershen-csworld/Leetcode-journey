def lcp(s,t):
    n,m = len(s),len(t)
    tb = [[0 for _ in range(m + 1)]for _ in range(n + 1 )]
    for i in range(n - 1,-1,-1):
        for j in range(m - 1,-1,-1):
            if s[i] == t[j]:
                tb[i][j] = tb[i + 1][j + 1] + 1
    print(tb[2][4])
lcp("abbbbbbb","bbbbbbbbbbbbbbb")