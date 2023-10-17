class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ### logn solution
        ###下標變化
        ###
        n = len(nums)
        l = 0
        r = n - 1
        #### breaking point
        while l < r:
            mid = l + r >> 1

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid
        if target >= nums[0]:
            l = 0
        else:
            r = n - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return r if nums[r] == target else - 1



s = Solution()
s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
