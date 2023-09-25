from random import *


class Treap:
    def __init__(self):
        self.sz = 1
        self.sum = 0
        self.ls = None
        self.rs = None
        self.val = 0
        self.prop = 0
        self.key = int(randrange(1, 100000))



def split(o, x):
    if o is None:
        return [None, None]
    ans = [None, None]
    pushdown(o)
    if size(o.ls) >= x:
        l, r = split(o.ls, x)
        o.ls = r
        ans = [l, o]
    else:
        l, r = split(o.rs, x - size(o.ls) - 1)
        o.rs = l
        ans = [o, r]
    pushup(o)
    return ans


def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    pushdown(a)
    pushdown(b)
    if a.key < b.key:
        pushdown(a)
        a.rs = merge(a.rs, b)
        pushup(a)
        return a
    else:
        b.ls = merge(a, b.ls)
        pushup(b)
        return b




def add_val(t, l, r, x):
    a1, a2 = split(t, r)
    b1, b2 = split(a1, l - 1)
    add_tag(b2, x)
    return merge(merge(b1, b2),a2)


def size(o):
    return o.sz if o else 0


def sum(o):
    return o.sum if o else 0


def pushdown(o):
    if o.prop > 0:
        o.val += o.prop
        if o.ls:
            add_tag(o.ls, o.prop)
        if o.rs:
            add_tag(o.rs, o.prop)
        o.prop = 0


def add_tag(o, val):
    o.prop += val
    o.sum = o.val +  o.prop * size(o)



def pushup(o):

    o.sz = 1 + size(o.ls) + size(o.rs)
    o.sum = sum(o.ls) + sum(o.rs) + o.val



def query(o, l, r):
    a1, a2 = split(o, r)
    b1, b2 = split(a1, l - 1)

    print(b2.sum)
    o = merge(merge(b1, b2),a2)
    return o


s = [1, 4, 2, 5, 2, 4, 5, 2]
root = None
cnt = 0
for i in s:
    if root is None:
        root = Treap()
        root.val = i
    else:
        newnode = Treap()
        newnode.val = i
        l,r = split(root,cnt)
        l = merge(l,newnode)
        root = merge(l,r)
    cnt += 1
#root = add_val(root, 2, 5, 5)
root = query(root, 2, 3)
