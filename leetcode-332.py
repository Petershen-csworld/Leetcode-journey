from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        g = defaultdict(list)
        for u, v in tickets:
            g[u].append(v)


        for item in g.items():
            g[item[0]].sort()
        res = []

        def dfs(cur):
            while len(g[cur]) > 0:
                nei = g[cur].pop(0)
                dfs(nei)
            res.append(cur)
        dfs("JFK")
        return res[::-1]


s = Solution()
s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
