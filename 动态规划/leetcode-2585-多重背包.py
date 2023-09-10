class Solution(object):
    def waysToReachTarget(self, target, types):
        """
        :type target: int
        :type types: List[List[int]]
        :rtype: int
        """
        C = target
        mod = pow(10, 9) + 7
        dp = [0 for _ in range(C + 1)]
        dp[0] = 1
        for count, marks in types:
            for j in range(target,0,-1):
                for k in range(1,min(count,j//marks) + 1):
                    dp[j] += dp[j - k * marks]
        return dp[C]


s = Solution()
s.waysToReachTarget(target = 18, types = [[6,1],[3,2],[2,3]]
                    )
