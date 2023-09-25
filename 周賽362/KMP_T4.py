
class Solution(object):
    def numberOfWays(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: int
        """

        def match(s):
            m = [0] * len(s)
            c = 0
            for i in range(1, len(s)):
                v = s[i]
                while c > 0 and s[c] != v:
                    c = m[c - 1]
                if s[c] == v:
                    c += 1
                m[i] = c
            return m

        def kmp_search(text, pattern):
            m = match(pattern)
            cnt = 0
            c = 0
            for i, v in enumerate(text):
                while c > 0 and pattern[c] != v:
                    c = m[c - 1]
                if pattern[c] == v:
                    c += 1
                if c == len(pattern):
                    cnt += 1
                    c = m[c - 1]
            return c
        def mul(a,b):
            c = [[0,0],[0,0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % (10 ** 9  7)
            return c
        def pow(a,n):
            res = [[1,0],[0,1]]
            while n:
                if n % 2 == 1:
                    res = mul(res,a)
                a = mul(a,a)
                n //= 2
            return res
        n = len(s)
        c = kmp_search(s + s[:-1],t)
        m = [[c - 1,c],[n - c, n -1 - c]]
        m = pow(m,k)
        return m[0][s != t]