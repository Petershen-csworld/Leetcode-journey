class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        g = [[] for _ in range(n)]
        vis = [False for _ in range(n)]
        for a,b in edges:
            if a in restricted or b in restricted:
                continue
            g[a].append(b)
            g[b].append(a)
        cnt = 0
        def dfs(cur):
            nonlocal cnt
            vis[cur] = True
            cnt += 1
            for nei in g[cur]:
                if not vis[nei]:
                    dfs(nei)
        dfs(0)
        return cnt