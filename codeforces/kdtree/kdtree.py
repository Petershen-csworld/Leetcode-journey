import math

K = 2


class kdnode:
    def __init__(self, data):
        self.val = data
        self.ls = None
        self.rs = None


def insert(o1, o2, k):
    if o1.val[k] < o2.val[k]:
        if o2.ls:
            insert(o1, o2.ls, (k + 1) % K)
        else:
            o2.ls = o1
            return
    else:
        if o2.rs:
            insert(o1, o2.rs, (k + 1) % K)
        else:
            o2.rs = o1
            return


def inrange(o1, reg):
    u, v = o1.val[0], o1.val[1]
    if reg[0] <= u <= reg[2] and reg[1] <= v <= reg[3]:
        return True
    return False



ans = []
def dist(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
def nearestnei(o,target,depth,best):
    if o is None:
        return best
    axis = depth % K
    next_best = None
    if best is None or dist(o.data,target) < dist(best.data,target):
        next_best = o
    else:
        next_best = best
    oppo = None
    if target[axis] < o.data[axis]:
        best = nearestnei(o.ls,target,depth + 1,next_best)
        oppo = o.rs
    else:
        best = nearestnei(o.rs,target,depth + 1,next_best)
        oppo = o.ls
    if dist(target,best.data) > abs(target[axis] - o.data[axis]):
        best = nearestnei(oppo,target,depth + 1,best)
    return best
def rangesearch(root,recmin,recmax,dpth):
    if not root:
        return
    axis = dpth % K
    if recmin[axis] <= root.val[axis] <= recmax[axis]:
        if all(recmin[i] <= root.val[i] <= recmax[i] for i in range(K)):
            ans.append(root.val)
    if recmin[axis] <= root.val[axis]:
        rangesearch(root.ls,recmin,recmax,dpth + 1)
    if recmax[axis] >= root.val[axis]:
        rangesearch(root.rs, recmin, recmax, dpth + 1)



nums = [[1, 4], [4, 5], [23, 45]]
root = kdnode(nums[0])
for i in range(1, len(nums)):
    newnode = kdnode(nums[i])
    insert(newnode, root, 0)

rangesearch(root, [1, 1],[29,50],0)
print(ans)
