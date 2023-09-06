class Solution(object):
    def longestCycle(self, g):
        """
        :type edges: List[int]
        :rtype: int
        """
        ## 圖中的最長環
        ## 内向基環樹
        n = len(g)

        deg = [0 for _ in range(n)]
        for u,v in enumerate(g):
            deg[v] += 1
        q = []
        for i in range(n):
            if deg[i] == 0:
                q.append(i)
        while len(q) > 0 :
                cur = q.pop(0)
                nei = g[cur]
                deg[nei] -= 1
                if deg[nei] == 0:
                    q.append(nei)
        ma = -1

        for i in range(n):
            if deg[i] > 0:
                cyc = 1
                cur = g[i]
                deg[cur] = -1
                while cur != i:
                    deg[cur] = -1
                    cur = g[cur]
                    cyc += 1

                ma = max(ma,cyc)

        return ma
s = Solution()
s.longestCycle([3,3,4,2,3])
