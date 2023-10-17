####
from collections import defaultdict

g = defaultdict(list)

color = [0 for _ in range(10010)]
dfn = [0 for _ in range(10010)]
low = [0 for _ in range(10010)]
onstack = [0 for _ in range(10010)]
inc = [0 for _ in range(10010)]
cnt = 0
num = 0
st = []
count = defaultdict(int)
def tarjan(x):
    global cnt
    global st
    global num
    low[x] = dfn[x] = cnt + 1
    onstack[x] = 1
    st.append(x)
    cnt += 1
    for nei in g[x]:
        if dfn[nei] == 0:
            tarjan(nei)
            low[x] = min(low[x],low[nei])
        elif onstack[nei] == 1:
            low[x] = min(low[x],dfn[nei])
    if low[x] == dfn[x]:
        num += 1
        while True:
            cur = st.pop()
            color[cur] = num
            onstack[cur] = 0
            count[num] += 1
            if cur == x:
                break

n,m = map(int,input().split())
for i in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
for i in range(1,n + 1):
    if color[i] == 0:
        tarjan(i)
for i in range(1,n + 1):
    for nei in g[i]:
        inc[nei] += 1
flag = 0
tmp = -1
for i in range(1,n+1):
    if inc[i] == 0:
        flag += 1
        tmp = i
if flag > 1:
   print(0)
else:
    print(count[tmp])