class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n//2
        def check(x):
            for i in range(x):
                if nums[i] >= nums[i - x]:
                    return False
                return True
        while l <= r:
            mid = l + r >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return len(nums) - 2*r
s = Solution()
s.minLengthAfterRemovals([2,3,4,4,4])
