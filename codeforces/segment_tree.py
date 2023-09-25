class Node:
    def __init__(self):
        self.ls = None
        self.rs = None
        self.sum = 0
        self.val = 0
        self.prop = 0

def add_tag(o,v,l,r):
    self.prop += x
    self.sum += x * (r - l + 1)
def sumof(o):
    return o.sum if o else 0
def pushup(o):
    o.sum = sumof(o.ls) + sum(o.rs) + o.val