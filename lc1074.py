from collections import defaultdict


class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        tot = 0
        m = len(matrix)
        n = len(matrix[0])
        s = [[0 for _ in range(n + 1)]for _ in range(m + 1)]
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + matrix[i - 1][j - 1]
        for top in range(1,m + 1):
            for bottom in range(top,m + 1):
                g = defaultdict(int)
                g[0] = 1
                for r in range(1,n + 1):
                    cursum = s[bottom][r] - s[top - 1][r]
                    tot += g[target - cursum]
        return tot