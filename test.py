import sys
from functools import cache

sys.setrecursionlimit(100000)
dp = [0 for _ in range(pow(10,6))]
pre =  [0 for _ in range(pow(10,6))]
dp[1] = 1
pre[2] = 1
def f(m,n):
    for i in range(2,m + 1):
        a = max(1,i - n)
        b = i - 1
        presum1 = pre[b + 1] - pre[a]
        dp[i] = presum1
        pre[i + 1] = pre[i] + dp[i]
f(5,3)

print(dp[3])
