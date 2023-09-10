from bisect import bisect_left

class Solution:
    def maximumMinutes(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        def check(t: int) -> bool:
            f = [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 1]
            fire = set(f)
            def spread_fire():
                nonlocal f
                tmp = f
                f = []
                for i, j in tmp:
                    for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in fire:
                            fire.add((x, y))
                            f.append((x, y))
            while t and f:
                spread_fire()  # 蔓延至多 t 分钟的火势
                t -= 1
            if (0, 0) in fire:  # 起点着火，寄
                return True

            q = [(0, 0)]
            vis = set(q)
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    if (i, j) not in fire:
                        for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in fire and (x, y) not in vis:
                                if x == m - 1 and y == n - 1:  # 我们安全了…暂时。
                                    return False
                                vis.add((x, y))
                                q.append((x, y))
                spread_fire()  # 蔓延 1 分钟的火势
            return True  # 寄

        ans = bisect_left(range(m * n + 1), True,check) - 1
        return ans if ans < m * n else 10 ** 9

