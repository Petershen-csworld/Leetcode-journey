class Solution(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        cnt =  0
        for i in range(n - 1):
            if nums[i] < i + 1 and nums[i + 1] > i + 1:
                cnt += 1
        if nums[n - 1] < n:
            cnt += 1
        return cnt