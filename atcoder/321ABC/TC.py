### digit dp
def check(s):
    for i in range(len(s) - 1):
        if int(s[i + 1]) >= int(s[i]):
            return False
    return True


def dfs(memo, numstr, curdigit, pre, isnum, islimit):
    l = len(memo)
    if curdigit == l:
        return 1 if isnum else 0
    if not islimit and isnum:
        if memo[curdigit][pre] >= 0:
            return memo[curdigit][pre]
    res = 0
    if not isnum:
        res += dfs(memo, numstr, curdigit + 1, pre, False, False)

    up = 9 if not islimit else int(numstr[curdigit])
    for i in range(0 if isnum else 1, up + 1):
        if not isnum or i <= pre - 1:
            res += dfs(memo, numstr, curdigit + 1, i, True, islimit & (i == up))
    return res


k = int(input())
l = 0
r = 9876543211
ans = -1
while l < r:
    mid = l + r + 1 >> 1
    memo = [[-1 for _ in range(10)] for _ in range(len(str(mid)))]
    ans = dfs(memo, str(mid), 0, 0, False, True)
    if ans <= k - 1:
        l = mid

    else:
        r = mid - 1

print(l + 1)