class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        for n in nums:
            if bin(n).count("1") == k:
                cnt += nums[n]
        return cnt
s = Solution()
s.sumIndicesWithKSetBits()