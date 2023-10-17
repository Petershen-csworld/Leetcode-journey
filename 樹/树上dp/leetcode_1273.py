from collections import defaultdict


class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        s = [0 for _ in range(nodes)]
        g = defaultdict(list)
        for i in range(nodes):
            if parent[i] != -1:
                g[parent[i]].append(i)

        def dfs(cur):
            sz = 1
            for nei in g[cur]:
                sz += dfs(nei)
                s[cur] += s[nei]
            s[cur] += value[cur]
            if s[cur] == 0:
                 sz = 0
            return sz
        return dfs(0)