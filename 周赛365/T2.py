from sortedcontainers import SortedList
class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pre = [0 for _ in range(n)]
        m = nums[0]

        for i in range(n):
            if nums[i] > m:
                m = nums[i]
            pre[i] = - min(nums[i] - m,0)
        ans = 0
        meet = 0
        print(pre)
        for i in range(1,n):
            ans = max(ans,meet * nums[i])
            if pre[i] > meet:
                meet = pre[i]
        print(ans)
        return ans
s = Solution()
s.maximumTripletValue([1000000,1,1000000])



