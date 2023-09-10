from itertools import permutations


class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cost = 0x3f3f3f3f
        togive = []
        toreceive = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    toreceive.append([i, j])
                if grid[i][j] > 1:
                    for k in range(grid[i][j] - 1):
                        togive.append([i, j])
        ### 匹配
        l = len(toreceive)
        for possi in list(permutations(togive)):
            c = 0
            possi = list(possi)
            for i in range(l):
                c += abs(possi[i][0] - toreceive[i][0]) + abs(possi[i][1] - toreceive[i][1])
            cost = min(cost, c)
            print(c)
        return cost


s = Solution()
s.minimumMoves(grid = [[1,3,0],[1,0,0],[1,0,3]])
