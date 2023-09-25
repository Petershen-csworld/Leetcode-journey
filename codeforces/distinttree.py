from collections import defaultdict

n, k =map(int ,input().split())
g = defaultdict(list)
for _ in range(n - 1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
dp = [[0] * (k + 1) for _ in range(n + 1)]
def dfs1(root,cur,fa,depth):
    if depth <= k:
        dp[root][depth] += 1
    for nei in g[cur]:
        if nei == fa:
            continue
        dfs1(root,nei,cur,depth + 1)
for i in range(1,n + 1):
    dfs1(i,i,-1,0)
res = 0
def dfs2(u,fa):
    global res
    res += dp[u][k]
    for v in g[u]:
        if v == fa:
            continue
        dp_u_0 = dp[u][0]
        branch = dp[v][1]
        dp[u][0] = dp_u_0 - branch

