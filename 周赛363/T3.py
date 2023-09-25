class Solution(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """
        m = len(cost)
        def check(num):
            for i in range(k):
                c = 0
                for j in range(m):
                    if stock[j] < num * composition[i][j]:
                        add = num * composition[i][j] - stock[j]
                        c += add * cost[j]
                if c <= budget:
                    return True
            return False



        l = 0
        r = pow(10,9)
        ans = -1
        while l < r:
            mid = l + r + 1>> 1
            if check(mid):
                ans = max(ans,mid)
                l = mid
            else:
                r = mid - 1
        return ans