from math import *


class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        l = 0
        r = int(1e14)
        ans = int(1e14)

        def cnt(num):
            return num // a + num // b - num // gcd(a, b)

        while l < r:
            mid = l + r >> 1
            if cnt(mid) >= n:
                r = mid
                ans = min(ans, r)
            else:
                l = mid + 1
        return ans % (pow(10, 9) + 7)
