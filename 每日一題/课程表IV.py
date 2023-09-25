class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        g = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            g[b].append(a)
        def dfs(cur,tar):
            if cur == tar:
                return True
            res = False
            for nei in g[cur]:
                res |= dfs(nei,tar)
            return res
        ans = []
        for a,b in queries:
            ans.append(dfs(a,b))
        return ans