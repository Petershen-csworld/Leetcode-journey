class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                r -= 1
            elif s > target:
                l += 1
            else:
                return [numbers[l],numbers[r]]
        return []