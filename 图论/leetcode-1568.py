from collections import defaultdict


class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def add_edge(a, b):
            for dirx, diry in dirs:
                newa, newb = a + dirx, b + diry
                if 0 < newa < m and 0 < newb < n:
                    if grid[newa][newb] == 1:
                        g[newa * n + newb].append(a * n + b)
                        g[a * n + b].append(newa * n + newb)

        ## m * n
        g = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    add_edge(i, j)
        dfn = [0 for _ in range(m * n)]
        low = [0 for _ in range(m * n)]
        st = []
        onstack = [False for _ in range(m * n)]
        boo = [True for _ in range(m * n)]
        cnt = 0
        scc = 0
        root = -1
        has_cut = False

        def tarjan(x):
            nonlocal cnt, onstack, dfn, low,has_cut
            dfn[x] = low[x] = cnt + 1
            cnt += 1
            st.append(x)
            onstack[x] = True
            flag = 0
            for nei in g[x]:
                if dfn[x] == 0:
                    tarjan(nei)
                    low[x] = min(low[x], low[nei])
                    if low[x] >= dfn[nei]:
                        flag += 1
                        if x != root or flag > 1:
                            boo[x] = True
                            has_cut = True
                elif onstack[nei]:
                    low[x] = min(low[x], dfn[nei])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tarjan(i * n + j)
        if has_cut:
            return 1
        else:
            return 2
s  = Solution()
s.minDays(grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]])