from collections import defaultdict


class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        #### dp[u][i] 代表以 u为字数的节点上labels为i的个数
        dp = [[0 for _ in range(26)] for _ in range(n)]

        def dfs1(cur, fa):
            curval = ord(labels[cur]) - ord('a')
            for nei in g[cur]:
                if nei == fa:
                    continue
                dfs1(nei, cur)
                for i in range(26):
                    dp[cur][i] += dp[nei][i]
            dp[cur][curval] += 1

        ans = [0 for _ in range(n)]


        dfs1(0, -1)
        for i in range(n):
            ans[i] = dp[i][ord(labels[i]) - ord('a')]
        return ans

s = Solution()
s.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab")
