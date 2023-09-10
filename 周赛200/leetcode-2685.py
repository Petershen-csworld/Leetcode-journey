from collections import defaultdict


class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        pa = [0 for _ in range(n)]
        pt = [1 for _ in range(n)]
        sz = [0 for _ in range(n)]
        gr = [[] for _ in range(n)]
        for i in range(n):
            pa[i] = i

        def find(a):
            if pa[a] != a:
                pa[a] = find(pa[a])
            return pa[a]

        def union(a, b):
            fa, fb = find(a), find(b)

            if fa == fb:
                edges[fb] += 1
                return
            else:
                pa[fa] = fb
                sz[fa] += sz[fb]
                edges[fa] += edges[fb] + 1

        for a, b in edges:
            union(a, b)
            gr[a].append(b)
            gr[b].append(a)
        for i in range(n):
            pa[i] = find(i)
        g = defaultdict(list)
        for i in range(n):
            g[pa[i]].append(i)
        cnt = 0
        for k in g.keys():
            flag = True
            for u in g[k]:
                for v in g[k]:
                    if u != v and u not in gr[v]:
                        flag = False
                if not flag:
                    break
            if flag:
                cnt += 1
        return cnt


s = Solution()
s.countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]])
