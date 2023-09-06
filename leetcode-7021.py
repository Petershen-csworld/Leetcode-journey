import bisect
import math
from collections import defaultdict


class Solution(object):
    def countKSubsequencesWithMaxBeauty(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        g = defaultdict(int)
        for ch in s:
            g[ch] += 1
        MOD = pow(10,9) + 7
        keyarr = list(g.keys())
        possi = len(g.keys())
        all_item = [item[1] for item in g.items()]
        all_item = sorted(all_item)
        tot = k
        ans = 1
        if k > possi:
            return 0
        def com(a,b):
            return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

        for i in range(possi - 1,-1,-1):
            cur = all_item[i]
            lft_cur = bisect.bisect_left(all_item,cur)

            if i - lft_cur + 1 > tot:
                num = i - lft_cur + 1
                ans = (ans * com(num,tot) * pow(cur,tot)) % MOD
                tot = 0
            if i - lft_cur + 1 <= tot:
                ans = (ans * cur) % MOD
                tot -= 1
            if tot == 0:
                break

        return ans % MOD

s = Solution()
s.countKSubsequencesWithMaxBeauty("jyuhiyzjuk",2)

