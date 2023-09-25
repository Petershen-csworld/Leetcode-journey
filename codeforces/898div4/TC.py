t = int(input())
def inring(x,y):
    return min(min(x + 1,10-x),min(y + 1,10-y))
while t > 0:
    a = []
    for _ in range(10):
        a.append(input())
    res = 0
    for i in range(10):
        for j in range(10):
            if a[i][j] == "X":
                res += inring(i,j)
    print(res)

    t -= 1