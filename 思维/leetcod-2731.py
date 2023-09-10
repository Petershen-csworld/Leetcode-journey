class Solution(object):
    def sumDistance(self, nums, s, d):
        """
        :type nums: List[int]
        :type s: str
        :type d: int
        :rtype: int
        """
        MOD = pow(10, 9) + 7
        for i, n in enumerate(nums):
            if n == "R":
                nums[i] += d
            else:
                nums[i] -= d
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i):
                ans += abs(nums[i] - nums[j])
                ans %= MOD
        return ans
