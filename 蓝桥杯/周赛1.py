from collections import defaultdict

t = int(input())
for i in range(t):
    s = input()
    g = defaultdict(int)
    for ch in s:
        g[ch] += 1
    if len(g.keys()) != 2:
        print("No")
    else:
        k = list(g.keys())
        k1,k2 = g[k[0]],g[k[1]]
        if (k1 == 1 and k2 == 3) or (k1 == 3 and k2 == 1):
            print("Yes")
        else:
            print("No")