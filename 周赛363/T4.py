import math
from collections import defaultdict
from math import sqrt


class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def isqrt(x):
            v=  int(math.sqrt(x))
            return v * v == x
        n = len(nums)
        first= int(sqrt(n))
        m = 0
        for i in range(first):
            m += nums[(i + 1) ** 2 - 1]
        for i in range(n):
            for j in range(i):
                if isqrt((i + 1) * ( j + 1)):
                    m = max(m, nums[i] + nums[j])
        return m

def decomp(x):
    g = defaultdict(int)
    i = 2
    while i * i < x:
        if x % i == 0:
            while x % i == 0:
                g[i] += 1
                x //= i
        i += 1
    if x > 1:
        g[x] += 1
    return g



s = Solution()
s.maximumSum(nums = [8,7,3,5,7,2,4,9])