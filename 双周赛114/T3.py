class Solution(object):
    def maxSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mn = nums[0]
        for v in nums:
            mn &= v
        cur = nums[0]
        cut = 0
        if mn == 0:
         for i in range(n):
            cur &= nums[i]
            if cur == mn:
                cut += 1
                if i != n - 1:
                    cur = nums[i + 1]
        else:
            return 1
        return cut
s = Solution()
s.maxSubarrays([22,21,29,22] )
print(22&21&29&22)
print(29&22)