n, x = map(int, input().split())
a = list(map(int, input().split()))
mi, ma = min(a), max(a)
s = sum(a)


def check(score):
    if score < mi:
        return s - ma >= x
    if score > ma:
        return s - mi >= x
    return s + score - ma - mi >= x


l = 0
r = 101
ans = 0x3f3f3f3f
while l < r:
    mid = l + r >> 1
    if check(mid):
        ans = min(ans, mid)
        r = mid
    else:
        l = mid + 1
print(ans if ans != 0x3f3f3f3f else -1)
