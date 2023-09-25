import functools
import math

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
pre = [0 for _ in range(n + 1)]
### pre[r + 1] - pre[l] = k
for i in range(n):
    pre[i + 1] = pre[i] ^ a[i]
cur = 0
### find number such that equals pre[r + 1] - k
N = 1 * pow(10, 6) + 100
bl = int(math.sqrt(n))


def cmp(a, b):
    if a[0] // bl == b[0] // bl:
        return a[1] > b[1]
    return a[0] // bl > b[0] // bl


q = []
for i in range(m):
    inp = list(map(int, input().split()))
    inp[0] -= 1
    q.append(inp)
q = sorted(q, key=functools.cmp_to_key(cmp))


def add(x):
    cnt = query(1, 0, N, pre[x] ^ k, pre[x] ^ k)
    update(1, 0, N, pre[x], 1)
    return cnt


def delete(x):
    update(1, 0, N, pre[x], -1)
    return query(1, 0, N, pre[x] ^ k, pre[x] ^ k)


seg = [0 for _ in range(4 * N + 5)]


def update(o, lc, rc, x, val):
    if lc >= rc:
        seg[o] += val
        return
    mid = lc + rc >> 1
    seg[o] += 1
    if mid >= x:
        update(o << 1, lc, mid, x, val)
    else:
        update(o << 1 | 1, mid + 1, rc, x, val)


def query(o, lc, rc, l, r):
    if l > rc or r < lc:
        return 0
    if lc >= l and rc <= r:
        return seg[o]
    mid = lc + rc >> 1
    ans = 0
    if l <= mid:
        ans += query(o << 1, lc, mid, l, r)
    if r > mid:
        ans += query(o << 1 | 1, mid + 1, rc, l, r)
    return ans


l = 1
r = 0
ans = 0
for a, b in q:
    while r < b:
        r += 1
        ans += add(r)
    while l > a:
        l -= 1
        ans += add(l)
    while r > b:
        ans -= delete(r)
        r -= 1
    while l < a:
        ans -= delete(l)
        l += 1
    print(ans)
