class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        :type receiver: List[int]
        :type k: int
        :rtype: int
        """
        n = len(receiver)
        klen = k.bit_length()
        par = [[0 for _ in range(klen + 1)] for _ in range(n)]
        f = [[0 for _ in range(klen + 1)] for _ in range(n)]
        for i in range(n):
            par[i][0] = receiver[i]
            f[i][0] = receiver[i]
        for i in range(klen ):
            for j in range(n):
                par[j][i + 1] = par[par[j][i]][i]
                f[j][i + 1] = f[j][i] + f[par[j][i]][i]
        m = 0
        for idx in range(n):
          l = 0
          cur = idx
          for i in range(klen):
            if (k >> i) & 1 > 0:
               l += f[cur][i]
               cur = par[cur][i]

          m = max(m,l + idx)
        return m
s = Solution()
s.getMaxFunctionValue([1,1,1,2,3], k = 3)