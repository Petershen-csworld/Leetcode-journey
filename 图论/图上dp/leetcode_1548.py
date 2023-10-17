from itertools import permutations
a = [0,1,2,3]
b = [1,2,3,4]
v = set()
for s in permutations(b):
    flag = True
    for i in range(4):
        for j in range(i + 1,4):
            if s[(i + j)%4] != (s[i] * s[j] + 5)%5:
                flag = False
    if flag:
        print(s)
