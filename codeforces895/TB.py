import bisect

t = int(input())
for _ in range(t):
    n = int(input())
    st = []
    for i in range(n):
        s,t = map(int,input().split())
        st.append([s,t])
    st.sort()
    l = 0
    r = pow(10,9)
    ans = -1
    def check(t):
        if t <= st[0][0]:
            return True
        for i in range(len(st)):
            if st[i][1] <= 2 * (t - st[i][0]):
                return False
        return True
    while l < r:
        mid = l + r + 1 >> 1
        if check(mid):
            ans = max(ans,mid)
            l = mid
        else:
            r = mid - 1
    print(ans)

