####網絡流板子拍出來
####最小費用最大流
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        src = m * n ##超级源点