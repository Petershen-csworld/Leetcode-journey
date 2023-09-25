from collections import defaultdict


class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        g = defaultdict(list)
        for u,v in edges:
            g[u].append([v,0])

            g[v].append([u,1])
        dp = [0 for _ in range(n)]
        def dfs(cur,fa):
            res = 0
            for nei,isrev in g[cur]:
                if nei == fa:
                    continue
                if isrev > 0:
                    res += 1
                res += dfs(nei,cur)
                dp[cur] = res
            return res
        dfs(0,-1)
        ans = [0 for _ in range(n)]
        def dfs1(cur,fa):
            ans[cur] = dp[cur]
            for nei,isrev in g[cur]:
                if  nei == fa:
                    continue
                if isrev > 0:
                    dp[nei] = ans[cur] - 1
                else:
                    dp[nei] = ans[cur] + 1
                dfs1(nei,cur)
        dfs1(0,-1)
        return ans
s = Solution()
s.minEdgeReversals(n = 4, edges = [[2,0],[2,1],[1,3]])




