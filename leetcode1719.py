from collections import defaultdict


class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        g = defaultdict(list)
        for a, b in pairs:
            g[a].append(b)
            g[b].append(a)
        n = len(g.keys())
        root = -1
        for i in g.keys():
            if len(g[i]) == n - 1:
                root = i
        if root == -1:
            return 0
        ans = 1
        for k in g.keys():
            if k == root:
                continue
            sz = len(g[k])
            psize = 0x3f3f3f3f3f
            par = -1
            for nei in g[k]:
                if sz <= len(g[nei]) < psize:
                    psize = len(g[nei])
                    par = nei
            if par == -1:
                return 0
            tmp  = g[par].copy()
            tmp.append(k)

            for item in g[k]:
                if item not in tmp:
                    return 0
            if psize == sz:
                ans = 2
        return ans
print([2,3].copy())