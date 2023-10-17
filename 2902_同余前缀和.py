from collections import Counter


class Solution(object):
    def countSubMultisets(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        tot = sum(nums)
        if l > tot:
            return 0
        cnt = Counter(nums)
        f = [cnt[0] + 1] + [0] * r
        del cnt[0]
        s = 0
        for x,c in cnt.items():
            s = min(r,s + x * c)
            for j in range(x,s + 1):
                f[j] = (f[j] + f[j - x]) % MOD
            for j in range(s,(c + 1) * x - 1,-1):
                f[j] = (f[j] - f[j - (c + 1)*x]) % MOD
        return sum(f[l:]) % MOD
