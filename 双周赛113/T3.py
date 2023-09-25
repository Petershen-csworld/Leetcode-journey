from collections import defaultdict


class Solution(object):
    def countPairs(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(k + 1):
            one = i
            ano = k - i
            g = defaultdict(int)
            for x, y in coordinates:
                res = 0
                res += g[(x ^ one, y ^ ano)]
                g[(x,y)] += 1
                ans += res
        return ans


s = Solution()
s.countPairs(coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0)
