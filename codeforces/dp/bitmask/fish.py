n = int(input())
p = [[] for _ in range(n)]
for i in range(n):
    p[i] = list(map(float, input().split()))
mask = (1 << n)
dp = [0 for _ in
      range(mask)]
dp[0] = 1
for day in range(n):
    for m in range(mask - 1, 0, -1):
        cnt = 0
        for i in range(n):
            if m & (1 << i) > 0:
                cnt += 1
        dp[m] = 0
        for i in range(n):
            for j in range(n):
                if m & (1 << i) > 0 and m & (1 << j) == 0:
                    dp[m] += dp[m & ~(1 << i)] * p[j][i] /((n - cnt)*(n - cnt + 1)/2)

print(' '.join([str(dp[(mask - 1) & ~(1 << i)]) for i in range(n) ]))

##cnt個死亡
## 原來: t = n - cnt + 1活著
## 吃掉概率為 C(t,2) = t * ()


###for i in range(n):
## for j in range(n):
### dp[i + 1][mask|j] = dp[i][mask] * p[i][j]
### dp[i + 1][mask |i] = dp[i][mask] * (1 - p[i][j])
