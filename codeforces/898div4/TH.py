from collections import defaultdict

t = int(input())
while t > 0:
    n,a,b = map(int,input().split())
    g = defaultdict(list)
    deg = [0 for _ in range(n + 1)]
    for _ in range(n):
        u,v = map(int,input().split())
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    q = []
    for _ in range(1,n + 1):
        if deg[_] == 1:
            q.append(_)
    while len(q) > 0:
        cur = q.pop()
        for nei in g[cur]:
            deg[nei] -= 1
            if deg[nei] == 1:
                q.append(nei)




    t -= 1






    t -= 1