from collections import defaultdict


class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        g = defaultdict(int)
        for u,v in pairs:
            g[u] += 1
            g[v] += 1
        tot = len(g.keys())
        root = -1
        for k in g.keys():
            if g[k] == tot - 1:
                root = k
        if root == -1:
            return 0
