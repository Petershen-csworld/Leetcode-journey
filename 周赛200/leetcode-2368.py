
class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        t = [0 for _ in range(26)]
        n = len(s)

        def off(ch):
            return ord(ch) - ord('a')
        t[off(s[0])] = 1
        res = -1
        for i in range(1,n):
            ma = -1
            for c in range(max(0,off(s[i]) - k),min(25,off(s[i]) + k)):
              ma = max(ma,t[c])
            cur = ma + 1
            t[off(s[i])] = cur
            res = max(res,cur)
        return res