from sortedcontainers import SortedList
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        s = SortedList()
        s.add(prices[0])
        for i in range(1,len(prices)):
            ans = max(ans, max(0, prices[i] - s[0]))
            s.add(prices[i])
        return ans

s = Solution()
s.maxProfit([7,1,5,3,6,4])
