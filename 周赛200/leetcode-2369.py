class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        f = [False] * (n + 1)
        f[0] = True
        ## f[i] 表示 nums[-] ~ nums[i]能组成有效划分
        for i in range(1,n):
            x = nums[i]
            if x == nums[i - 1]:
                if f[i - 1]:
                    f[i + 1] = True
            if i > 1:
                if f[i - 2] and x == nums[i - 1] == nums[i - 2]:
                    f[i + 1] = True
                if f[i - 2] and x == nums[i - 1] + 1== nums[i - 2] + 2:
                    f[i + 1] = True
        return f[n]