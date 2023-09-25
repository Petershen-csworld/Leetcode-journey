from collections import defaultdict

n = int(input())
g = defaultdict(list)
w = list(map(int, input().split()))
for i in range(n - 1):
    u, v, c = map(int, input().split())
    g[u].append([v, c])
    g[v].append([u, c])
ans = 0

def dfs1(cur, fa):
    global ans
    m = 0
    mm = 0
    for nei, c in g[cur]:
        if nei == fa:
            continue
        val = dfs1(nei,cur) - c
        if  val > m:
            mm = m
            m = val
        elif val > mm:
            mm = val
    ans = max(ans,w[cur - 1] + m + mm)

    return max(m,mm) + w[cur - 1]


dfs1(1, -1)
print(ans)
