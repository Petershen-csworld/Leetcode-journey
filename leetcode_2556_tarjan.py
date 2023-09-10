from collections import defaultdict


class Solution(object):
    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m,n = len(grid),len(grid[0])
        dirs = [[0,1],[1,0]]
        g = defaultdict(list)
        for i in range(m):
            for j in range(n):
                for dir in dirs:
                    x = i + dir[0]
                    y = j + dir[1]
                    if x < m and y < n and grid[i][j] == 1 and grid[x][y] == 1:
                         g[i * m + j].append(x * m + y)
        onstack = [False for _ in range(m * n)]
        ids = [-1 for _ in range(m * n)]
        low = [0x3f3f3f3f for _ in range(m * n)]
        cnt = 1
        st = []
        ans = False
        def tarjan(at):
            nonlocal cnt,ans
            low[at] = ids[at] = cnt
            cnt += 1
            st.append(at)
            onstack[at] = True
            for nei in g[at]:
                if ids[nei] != -1:
                    tarjan(nei)
                if onstack[nei]:
                    low[at] = min(low[at],low[nei])
                if low[nei] > ids[at]:
                    print(at)
                    print(nei)
                    ans = True
            if low[at] == ids[at]:
              while True:
                curnode = st.pop()
                st[curnode] = False
                low[curnode] = ids[curnode]
                if curnode == at:
                    break
              ## scccnt += 1
        return ans





