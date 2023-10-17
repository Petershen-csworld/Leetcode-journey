import io,os
t = int(input())
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    q = int(input())
    sum1 = [0 for _ in range(4 * n + 10)]
    sum2 = [0 for _ in range(4 * n + 10)]
    tag = [0 for _ in range(4 * n + 10)]


    def push_up(o):
        sum1[o] = sum1[o << 1] ^ sum1[o << 1 | 1]
        sum2[o] = sum2[o << 1] ^ sum2[o << 1 | 1]


    def add_tag(o):
        tag[o] ^= 1
        tmp = sum2[o]
        sum2[o] = sum1[o]
        sum1[o] = tmp


    def push_down(o):
        if tag[o] > 0:
            add_tag(o << 1)
            add_tag(o << 1 | 1)
            tag[o] = 0


    def build(o, pl, pr):
        if pl == pr:
            if s[pl] == "0":
                sum1[o] ^= a[pl]
            else:
                sum2[o] ^= a[pl]
            return
        mid = pl + pr >> 1
        build(o << 1, pl, mid)
        build(o << 1 | 1, mid + 1, pr)
        push_up(o)


    def update(o, pl, pr, l, r):
        if l <= pl and pr <= r:
            add_tag(o)
            return
        if l > pr or r < pl:
            return
        push_down(o)
        mid = pl + pr >> 1
        if l <= mid:
            update(o << 1, pl, mid, l, r)
        if r > mid:
            update(o << 1 | 1, mid + 1, pr, l, r)
        push_up(o)


    build(1, 0, n - 1)
    res = ""
    for _ in range(q):

        op = list(map(int, input().split()))
        if op[0] == 1:
            update(1, 0, n - 1, op[1] - 1, op[2] - 1)
        if op[0] == 2:

            if op[1] == 0:
                res += str(sum1[1]) + " "
            else:
                res += str(sum2[1]) + " "
    print(res)
    t -= 1
