b = [3,2,1,3,2,1,3,1,1,1,2,1,2,1,2,3,3,1]
b = b *10
n = len(b)
pre= [ 0 for _ in range(n + 1)]
for i in range(n):
    pre[i + 1] = pre[i] + b[i]



for i in range(n):
    for j in range(i):
        if pre[i] - pre[j] == 78:
            print(str(i) + "-" + str(j))