from collections import defaultdict
from functools import cmp_to_key


class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def cmp(a,b):
            if len(a) > len(b):
                return 1
            elif len(a) < len(b):
                return -1
            n = len(a)
            for i in range(n):
                if int(a[i]) > int(b[i]):
                    return 1
                elif int(a[i]) < int(b[i]):
                    return -1
            return 0
        res = []
        n = len(s)
        pre = [0 for _ in range(n + 1)]

        for i in range(n):
            pre[i + 1] = pre[i] + (1 if s[i] == "1" else 0)
        for i in range(1,n + 1):
            for j in range(i):
                if pre[i] - pre[j] == k:
                    res.append(s[j:i])

        res = sorted(res,key = cmp_to_key(cmp))


        return res[0]
s = Solution()
s.shortestBeautifulSubstring(s = "100011001", k = 1)