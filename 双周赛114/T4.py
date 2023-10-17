from collections import defaultdict


class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        s = [0 for _ in range(n)]
        add = [0 for _ in range(n)]
        def dfs1(u,fa):
            s[u] = values[u]
            for nei in g[u]:
                if nei == fa:
                    continue
                dfs1(nei,u)
                if s[nei] % k != 0:
                    s[u] += s[nei]
                else:
                    add[u] += 1
            if add[u] % k == 0:
                add[u] += 1
        return add[0]



