from collections import defaultdict


class Solution(object):
    def __init__(self):
        N = int(1e5)
        self.is_prime = [True] * (N + 1)  # have 0
        self.is_prime[0] = self.is_prime[1] = False
        self.prime = []
        for n in range(2, N + 1):
            if self.is_prime[n]:
                self.prime.append(n)
            for p in self.prime:
                if p * n > N:  # Index out of range
                    break
                self.is_prime[p * n] = False
                if n % p == 0:
                    break

    def countPaths(self, t, edges):

        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(cur, fa):
            sz = 1
            for v in g[cur]:
                if fa == v:
                    continue
                if not self.is_prime[v]:
                    sz += dfs(v, cur)
            return sz

        tot = 0
        i = 0

        while self.prime[i] <= t and i < len(self.prime):
            res = []
            np = 0
            for nei in g[self.prime[i]]:
                if not self.is_prime[nei]:
                    val = dfs(nei, i)
                    res.append(val)
                    np += val
            for j in range(len(res)):
                for k in range(j):
                    tot += res[j] * res[k]
            tot += np
            i += 1
        return tot


s = Solution()
s.countPaths(5, [[1, 3], [4, 3], [2, 3], [5, 2]])
s.countPaths(6, [[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]])
s.countPaths(5,   [[1,2],[1,3],[2,4],[2,5]])
res = [3,2,2]
a = 0
for j in range(len(res)):
    for k in range(j):
        a += res[j] * res[k]
print(a)
