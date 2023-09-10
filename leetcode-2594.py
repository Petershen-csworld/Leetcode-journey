import math
from collections import defaultdict


class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        g = defaultdict(list)

        for i, r in enumerate(ranks):
            g[r].append(i)

        def check(t):
            res = 0
            for idx in g.keys():
                res += int(math.sqrt(t // idx)) * len(g[idx])
            return res >= cars

        ans = 0x3f3f3f3f3f
        l = 0
        r = pow(10, 10)
        while l < r:
            mid = l + r >> 1
            if check(mid):
                ans = min(ans,mid)
                r = mid
            else:
                l = mid + 1
        return ans


s = Solution()
s.repairCars(ranks = [4,2,3,1], cars = 10)
