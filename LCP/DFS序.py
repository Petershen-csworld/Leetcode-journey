from collections import defaultdict

n = 10
num = [0 for _ in range(11)]
cnt = 0

g = defaultdict(list)
for u

def dfs(cur, fa):
    nonlocal cnt
    for nei in g[cur]:
        if nei != fa:
            dfs(nei, cur)
    num[cur] = cnt
    cnt += 1
print(cnt)
