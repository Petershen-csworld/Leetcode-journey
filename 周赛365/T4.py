
class Solution(object):
    def countVisitedNodes(self, edges):
        """
        :type edges: List[int]
        :rtype: List[int]
        """
        n = len(edges)
        inc = [0 for _ in range(n)]
        for i in range(n):
            inc[edges[i]] += 1
        def topo():
            q = []
            for i in range(n):
                if inc[i] == 0:
                    q.append(i)
            while len(q) > 0:
                cur = q[-1]
                q.pop()
                nei = edges[cur]

                inc[nei] -= 1
                if inc[nei] == 0:
                        q.append(nei)

        topo()
        def dfs(cur):
            if inc[cur] > 0:
                return 1
            res = 0
            res += dfs(edges[cur])
            return res
        circle = 0
        for i in range(n):
            circle += 1 if inc[i] > 0 else 0
        ans= [0 for _ in range(n)]
        for i in range(n):
            if inc[i] > 0:
                ans[i] = circle
            else:
                ans[i] = circle + dfs(i)
        return ans
s = Solution()
s.countVisitedNodes([3 ,6 ,1 ,0 ,5 ,7 ,4 ,3])
## [2,2,3,2,3,4,2,3,3]
## [3 ,6 ,1 ,0 ,5 ,7 ,4 ,3]