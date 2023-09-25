from collections import defaultdict

n = int(input())
g = defaultdict(list)
a = list(map(int,input().split()))
p = list(map(int,input().split()))
for i in range(n - 1):
    g[i + 1].append(a[i])
    g[a[i]].append(i + 1)
dp = [0 for _ in range(n)]
def dfs(cur,fa,isfull):

    if len(g[cur]) == 1:
        return 1
    res = 0

    for nei in g[cur]:
        if nei == fa:
            continue

        ###
        nextfull = (p[nei] == 1)
        if isfull and not nextfull:
            res += dfs(nei,cur,isfull) + dfs(nei,cur,nextfull) ##當前地方切割

        else:
            res +=  dfs(nei,cur,nextfull)

    return res

