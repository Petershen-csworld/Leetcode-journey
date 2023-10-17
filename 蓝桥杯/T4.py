n,m,q = map(int,input().split())
time = list(map(int,input().split()))
N = int(2e5) + 10
t = [0 for _ in range(N)]
for i in range(N):
    t[i] += t[i - 1]
dp = [0 for _ in range(N)]
w = [0 for _ in range(m)]
s = [0 for _ in range(n)]
for i in range(m):
    w[i],s[i] = map(int,input().split())

for i in range(m):
    for c in range(1 << w[i],n + 1):
        val = 1 << w[i]
        if t[c] - t[c - val] == 0:
            dp[c] = max(dp[c],dp[c - val] + s[i])
print(dp)
