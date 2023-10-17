class Solution(object):
    def maxSumSubmatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j] += pow(10, 5)
        target += pow(10, 5)
        ans = -0x3f3f3f3f
        for i in range(m):
            v = [0 for _ in range(n)]
            for j in range(i, -1, -1):
                for k in range(n):
                    v[k] += matrix[j][k]
                l = 0
                sumt = 0
                for idx in range(n):
                    sumt += v[idx]
                    while sumt > target and l < idx:
                        sumt -= v[l]
                        l += 1

                    if sumt <= target:
                        ans = max(sumt, ans)
            return ans - pow(10, 5)


s = Solution()
s.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2)
