import math

t = int(input())
for i in range(t):
    n,x,y = map(int,input().split())
    ma = n // x - n // math.lcm(x,y)
    mi = n //y - n // math.lcm(x,y)
    lsum = 0
    rsum = 0
    for i in range(ma):
        lsum += n - i
    for i in range(mi):
        rsum += i + 1
    print(lsum - rsum)


