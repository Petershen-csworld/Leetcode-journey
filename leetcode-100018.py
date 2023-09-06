class Solution(object):
    def minOperationsQueries(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        m = n.bit_length()
        p = [[-1] * m for _ in range(n)]
        depth = [0] * n
        cnt = [[[0] * 26 for _ in range(m)] for _ in range(n)]
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append([y, w - 1])
            g[y].append([x, w - 1])

        def dfs(cur, fa):
            p[cur][0] = fa
            for y, w in g[cur]:
                if y != fa:
                    cnt[y][0][w] = 1
                    depth[y] = depth[cur] + 1
                    dfs(y,cur)
        dfs(0, - 1)

        for i in range(m - 1):
            for j in range(n):
                pa = p[j][i]
                if pa != -1:
                    ppa = p[pa][i]
                    p[j][i + 1] = ppa
                    for idx , (c1,c2) in enumerate(zip(cnt[j][i],cnt[pa][i])):
                        cnt[j][i + 1][idx] = c1 + c2
        ans = []
        for x,y in queries:
            pathlen = depth[x] + depth[y]
            cw = [0] * 26
            if depth[x] > depth[y]:
                x,y = y ,x
            k = depth[x] - depth[y]
            for i in range(k.bit_length()):
                    if  (k >> i) & 1:
                        pa = p[y][i]
                        for j,c in enumerate(cnt[y][i]):
                            cw[j] += c
                        y = pa
            if y != x:
                    for i in range(m - 1,-1,-1):
                        px , py = p[x][i] , p[y][i]
                        if px != py:
                            for j ,(c1,c2) in enumerate(zip(cnt[x][i],cnt[y][i])):
                                cw[j] += c1 + c2
                            x,y = px,py
                    for j,(c1,c2) in enumerate(zip(cnt[x][0],cnt[y][0])):
                        cw[j] += c1 + c2
                    x = p[x][0]
            lca = x
            pathlen -= 2 * depth[lca]
            ans.append(pathlen - max(cw))
        return ans
s = Solution()
s.minOperationsQueries(n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]])

