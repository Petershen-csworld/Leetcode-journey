from collections import defaultdict

g = defaultdict(list)


def construct(edges):
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)


##
e = [[0, 1], [1, 2], [0, 3]]
construct(e)

n = len(g.keys())
depth = [0 for _ in range(n)]
sz = [1 for _ in range(n)]
son = [-1 for _ in range(n)]
top = [0 for _ in range(n)]
dfn = [0 for _ in range(n)]
pa = [-1 for _ in range(n)]


def dfs1(cur, fa):
    mson = -1
    for nei in g[cur]:
        if nei != fa:
            depth[nei] = depth[cur] + 1
            pa[nei] = cur
            dfs1(nei, cur)
            sz[cur] += sz[nei]
            if sz[nei] > mson:
                mson = sz[nei]
                son[cur] = nei


cnt = 0


def dfs2(now, t):
    global cnt
    top[now] = t
    dfn[now] = cnt
    cnt += 1
    if son[now] == -1:
        return
    dfs2(son[now], now)
    for neib in g[now]:
        if neib != pa[now] and neib != son[now]:
            dfs2(neib, neib)


class node:
    def __init__(self):
        self.sum = 0
        self.mx = 0


tr = [node() for _ in range(10000)]


def update(o, lc, rc, x, val):
    if lc == rc:
        tr[o].sum = tr[o].mx = val
        return
    mid = lc + rc >> 1
    if x <= mid:
        update(o << 1, lc, mid, x, val)
    if x > mid:
        update(o << 1 | 1, mid + 1, rc, x, val)
    tr[o].mx = max(tr[o << 1].mx, tr[o << 1 | 1].mx)
    tr[o].sum = tr[o << 1].sum + tr[o << 1 | 1].sum


def ask(o, lc, rc, l, r):
    if lc >= l and rc <= r:
        return tr[o].sum
    if rc < l or lc > r:
        return 0
    ans = 0
    mid = lc + rc >> 1
    if l <= mid:
        ans += ask(o << 1, lc, mid, l, r)
    if r > mid:
        ans += ask(o << 1 | 1, mid + 1, rc, l, r)
    return ans


depth[0] = 1

dfs1(0, -1)
dfs2(0, 0)
### 0 1 2 3
num = [1, 2, 3, 2]
for i in range(len(num)):
    update(1, 0, n - 1, dfn[i], num[i])



def querysum(x, y):
    res = 0
    while top[x] != top[y]:
        if depth[x] < depth[y]:
            x, y = y, x
        res += ask(1, 0, n - 1, dfn[top[x]], dfn[x])
        x = pa[top[x]]
    if dfn[x] > dfn[y]:
        x, y = y, x
    res += ask(1, 0, n - 1, dfn[x], dfn[y])
    return res


###  1(0)
##  /  \
## 2(1)  2(3)
## /
## 3(2)
## e = [[0, 1], [1, 2], [0, 3]]
print(top)
print(querysum(0, 2))
