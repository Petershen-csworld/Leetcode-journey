n,k = map(int,input().split())
h = list(map(int,input().split()))

l = -1
r = int(1e9) + 10
def check(num):
    tot = 0
    curmax = -1
    curmin = 0x3f3f3f3f
    for i in range(n):
        curmax = max(curmax,h[i])
        curmin = min(curmin,h[i])
        if curmax - curmin > num:
            tot += 1
            curmax = h[i]
            curmin = h[i]
    return tot <= k


ans = 0x3f3f3f3f3f
while l < r:
    mid = l + r >> 1
    if check(mid):
        ans = min(ans,mid)
        r = mid
    else:
        l = mid + 1

print(ans)
