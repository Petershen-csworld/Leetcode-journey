class Solution(object):
    def minimumTotalPrice(self, n, edges, price, trips):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :type trips: List[List[int]]
        :rtype: int
        """
        g = [[] for _ in range(n)]
        date = [0 for _ in range(n)]
        depth = [0 for _ in range(n)]
        m = n.bit_length()
        pa = [[-1 for _ in range(m + 1)] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs1(cur, fa):
            pa[cur][0] = fa
            for nei in g[cur]:
                if nei != fa:
                    depth[nei] = depth[cur] + 1
                    dfs1(nei, cur)
        def dfs2(cur,fa):
            not_hav,hav,cnt = 0,0,date[cur]
            for y in g[cur]:
                if y != fa:
                    nh,h,c = dfs2(y,cur)
                    not_hav += min(h,nh)
                    hav += nh
                    cnt += c
            not_hav += price[cur] * cnt
            hav += price[cur] * cnt // 2
            return not_hav,hav,cnt


        dfs1(0, -1)
        for i in range(m):
            for j in range(n):
                p = pa[j][i]
                if p != -1:
                    pa[j][i + 1] = pa[p][i]

        def lca(x, y):
            if depth[x] > depth[y]:
                x, y = y, x
            k = depth[y] - depth[x]
            for i in range(k.bit_length()):
                if (k >> i) & 1:
                    y = pa[y][i]
            if y != x:
              for i in range(m - 1, -1, -1):
                px, py = pa[x][i], pa[y][i]
                if px != py:
                    x, y = px, py
                return pa[y][0]
            return x
        for x,y in trips:
            date[x] += 1
            date[y] += 1
            lc = lca(x,y)
            date[lc] -= 1
            if pa[lc][0] != -1:
                date[pa[lc][0]] -= 1
        nh,h,c = dfs2(0,-1)
        return min(nh,h)

s = Solution()
s.minimumTotalPrice(n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]])