from functools import cache

from sortedcontainers import SortedList


class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = SortedList()
        n = len(arr)
        ## dp[i][0]表示當前索引為i , 下一步為第奇數次跳法的位置
        ## dp[i][1]表示當前索引為i , 下一步為第偶數次跳的位置
        dp = [[False,False] for _ in range(n)]
        dp[n - 1][0] = dp[n - 1][1] = True
        s.add([arr[n - 1] , n - 1])
        for i in range(n - 2, -1,-1):
            



s = Solution()
a = [1,1,1,3]

s.oddEvenJumps(a)
