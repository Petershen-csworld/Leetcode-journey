from collections import defaultdict


class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        m = len(g.keys())
        n = len(edges)
        vis = [False for _ in range(n)]

        def dfs(cur, fa, u, v):
            curval = nums[cur]
            vis[cur] = True
            for nei in g[cur]:
                if nei == fa or (cur, fa) == (u, v) or (cur, fa) == (v, u):
                    continue
                curval ^= dfs(nei, cur, u, v)
            return curval

        for i in range(n):
            for j in range(i, n):
                vis = [False for _ in range(n)]
                for i in range(n):
                    if not vis[i]:
                        dfs(i, -1, edges[i])
