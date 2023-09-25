import functools
import math

n, t = map(int, input().split())
a = list(map(int, input().split()))
q = []
for i in range(t):
    u, v = map(int, input().split())
    q.append([u - 1, v - 1])
bl = int(math.sqrt(n))


def cmp(a, b):
    if a[0] // bl == b[0] // bl:
        return a[1] > b[1]
    return a[0] // bl > b[0] // bl


bit = [0 for _ in range(pow(10, 6) + 5)]


def lowbit(x):
    return x & (-x)


def update(x, val):
    while x < pow(10, 6) + 5:
        bit[x] += val
        x += lowbit(x)


def query(x):
    res = 0
    while x > 0:
        res += bit[x]
        x -= lowbit(x)
    return res


q = sorted(q, key=functools.cmp_to_key(cmp))


def add(x):

    cnt = query(a[x]) - query(a[x] - 1)
    update(a[x], 1)
    return cnt


def delete(x):

    update(a[x], -1)
    return query(a[x]) - query(a[x] - 1)


l = 0
r = -1
ans = 0
for s, t in q:
    while r < t:
        r += 1
        inc = add(r)
        ans += (2 * inc + 1) * a[r]


    while l > s:
        l -= 1
        inc = add(l)
        ans += (2 * inc + 1) * a[l]

    while r > t:
        inc = delete(r)
        ans -= (2 * inc + 1) * a[r]
        r -= 1

    while l < s:
        inc = delete(l)
        ans -= (2 * inc + 1) * a[l]
        l += 1

    print(ans)
