from collections import defaultdict


class Solution(object):
    def minTrioDegree(self, n, edges):
        g = defaultdict(list)
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        inc = [0 for _ in range(n + 1)]
        for u, v in edges:
            inc[u] += 1
            inc[v] += 1
        res = 0x3f3f3f3f
        for u, v in edges:
            if inc[u] > inc[v]:
                g[u].append(v)
            elif inc[u] == inc[v]:
                if u < v:
                    g[u].append(v)
                else:
                    g[v].append(u)
            else:
                g[v].append(u)
        for i in range(1,n + 1):
            for j in g[i]:
                for k in g[j]:
                    if k in g[i]:
                        res = min(res, inc[i] + inc[j] + inc[k] - 6)
        return res if res != 0x3f3f3f3f else -1
