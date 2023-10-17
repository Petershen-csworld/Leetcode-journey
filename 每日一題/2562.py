class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tot = 0
        for i in range(n//2):
            tot += int(str(nums[i]) + str(nums[n - i - 1]))
        if n % 2:
            tot += nums[n//2]
        return tot