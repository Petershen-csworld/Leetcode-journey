class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        m = len(grid)
        n = len(grid[0])
        pre = [0 for _ in range(m * n)]
        suf = [0 for _ in range(m * n)]
        pre[0] = grid[0][0]
        for i in range(1,m * n):
            idx = i // n
            off = i - n * idx
            pre[i] = pre[i - 1] * grid[idx][off] % MOD
        suf[m * n - 1] = grid[m - 1][n - 1]
        for i in range(m * n - 2,-1,-1):
            idx = i // n
            off = i - n * idx
            suf[i] = suf[i + 1] * grid[idx][off] % MOD
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m * n):
            idx = i // n
            off = i - n * idx
            if i == 0:
                ans[idx][off] = suf[1]
            elif i == m * n - 1:
                ans[idx][off] = pre[m * n - 2]
            else:

                ans[idx][off] = suf[i + 1] * pre[i - 1] % MOD
        return ans
s = Solution()
s.constructProductMatrix(grid = [[1,2],[3,4]])