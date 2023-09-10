from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        g = defaultdict(list)
        deg = [0 for _ in range(n)]
        for a,b in prerequisites:
            g[b].append(a)
        q = []
        for i in range(n):
            if deg[i] == 0:
                q.append(i)
        while len(q) > 0:
            cur = q.pop()
            for nei in g[cur]:
                deg[nei] -= 1
                if deg[nei] == 0:
                    q.append(nei)
        for i in range(n):
            if deg[i] > 0:
                return False
        return True