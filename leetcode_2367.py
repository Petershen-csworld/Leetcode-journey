
class Solution(object):
    def arithmeticTriplets(self, nums, diff):

        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j + 1,n):
                         if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                           cnt += 1
        return cnt

