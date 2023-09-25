t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int,input().split()))
    mi = 0x3f3f3f3f
    midx = -1
    pro = 1
    for i,n in enumerate(a):
        if n < mi:
            mi = n
            midx = i
    a[midx] += 1
    for n in a:
        pro *= n
    print(pro)
    t -= 1