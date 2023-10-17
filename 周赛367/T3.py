import bisect

from sortedcontainers import SortedList


class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        n = len(nums)
        curmax = [-0x3f3f3f3f,-1]
        curmin = [0x3f3f3f3f,-1]
        j = 0
        for i in range(n):

           cur = nums[i]
           while i - j >= indexDifference:
               if nums[j] > curmax[0]:
                   curmax = [nums[j],j]
               if nums[j] < curmin[0]:
                   curmin = [nums[j],j]
               j += 1
           if curmax[0] >= nums[i] + valueDifference:
               return [curmax[0],i]
           if curmin[0] >= nums[i] + valueDifference:
               return [curmin[0], i]

        return [-1,-1]
s = Solution()
s.findIndices([0,4,7,2],2,7)


