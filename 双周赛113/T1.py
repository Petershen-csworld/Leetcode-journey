class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def check_inc(l,r):
            for idx in range(l + 1,r + 1):
                if nums[idx] < nums[idx - 1]:
                    return False
            return True
        for u in range(n):
            if check_inc(0,n -1):
                return u
            f = nums.pop()
            nums.insert(0,f)
        return -1
a = [1,2,3]
