##  https://codeforces.com/gym/100551/problem/A
N, K = map(int,input().split())
st = []
p = [i for i in range(N)]
sz = [1 for i in range(N)]
def find(x):
    while x != p[x]:
        x = p[x]
    return p[x]

def union(a,b):
    fa,fb = find(a),find(b)
    if fa == fb:
        return
    if sz[fa] > sz[fb]:
        fa, fb = fb, fa
    p[fa] = fb
    sz[fa] += sz[fb]
def query():
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    return cnt
def
for i in range(K):
    op = input()
    if op == "?":
        print(query())
    if op == "+":


