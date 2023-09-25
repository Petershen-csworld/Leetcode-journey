####網絡流板子拍出來
####最小費用最大流
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        src = m * n  ##超级源点
        dst = m * n + 1



        g = [[] for _ in range(m * n + 2)]
        cos = [[0 for _ in range(m * n + 2)] for _ in range(m * n + 2)]
        capa = [[0 for _ in range(m * n + 2)] for _ in range(m * n + 2)]

        def addedge(u, v, cap, cost):
            g[u].append(v)
            g[v].append(u)
            capa[u][v] = cap
            capa[v][u] = 0
            cos[u][v] = cost
            cos[v][u] = -cost

        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1:
                    addedge(src, i * n + j, grid[i][j] - 1, 0)
                    for k in range(3):
                        for l in range(3):
                            if grid[k][l] == 0:
                                addedge(i * n + j, k * n + l, 1, abs(k - i) + abs(l - j))
                if grid[i][j] == 0:
                    addedge(i * n + j, dst, 1, 0)

        def spfa(v, dist, pa):
            q = [v]
            N = len(dist)
            inq = [False for _ in range(N)]
            dist[v] = 0
            while len(q) > 0:
                cur = q.pop()
                inq[cur] = False
                for nei in g[cur]:

                    if capa[cur][nei] > 0 and dist[nei] >  dist[cur] + cos[cur][nei]:
                        dist[nei] = dist[cur] + cos[cur][nei]

                        pa[nei] = cur
                        if not inq[nei]:
                            q.append(nei)
                            inq[nei] = True



        def maxflow():
            flow = 0
            cost = 0
            while True:

                dist = [0x3f3f3f3f for _ in range(m * n + 2)]
                pa = [-1 for _ in range(m * n + 2)]
                spfa(src, dist, pa)


                if dist[dst] == 0x3f3f3f3f:
                    break
                v = dst
                mflow = 0x3f3f3f3f
                while v != src:
                    mflow = min(mflow,capa[pa[v]][v])
                    v = pa[v]
                v = dst
                while v != src:
                    capa[pa[v]][v] -= mflow
                    capa[v][pa[v]] += mflow
                    v = pa[v]
                flow += mflow
                cost += mflow * dist[dst]
            return cost
        return maxflow()
s = Solution()
s.minimumMoves(grid = [[1,1,0],[1,1,1],[1,2,1]])
