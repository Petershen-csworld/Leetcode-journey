class Solution:
    def maximumSumOfHeights(self, maxHeights) -> int:
        n = len(maxHeights)
        res = 0
        ans = [0 for _ in range(n)]
        for i in range(n):
            peak = maxHeights[i]

            ans[i] = peak
            for pre in range(i - 1,-1,-1):
                ans[pre]= max(1,min(maxHeights[pre],ans[pre + 1]))
            for pre in  range(i + 1,n):
                ans[pre]= max(1,min(maxHeights[pre],ans[pre - 1]))
            res = max(res,sum(ans))
        return res
s = Solution()
s.maximumSumOfHeights([6,5,3,9,2,7])
####  333 9 22