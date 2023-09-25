class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        ###網絡流板子題
        N = len(nums)
        g = [[] for _ in range(numSlots + N + 2)]
        capa = [[0 for _ in range(numSlots + N + 2)] for _ in range(numSlots + N + 2)]
        cost = [[0 for _ in range(numSlots + N + 2)] for _ in range(numSlots + N + 2)]

        def add(u, w, cap, c):
            g[u].append(w)
            g[w].append(w)
            capa[u][w] = cap
            capa[w][u] = 0
            cost[u][w] = c
            cost[w][u] = -c

        src = 0
        dst = numSlots + N + 1

        for i in range(1, N + 1):
            add(src, i, 1, 0)
        for i in range(1, N + 1):
            for j in range(N + 1, numSlots + N + 1):
                add(i, j, 0x3f3f3f3f, (nums[i - 1] & (j - N)) * -1)
        for i in range(N + 1, numSlots + N + 1):
            add(i, dst, 2, 0)

        def spfa(d, fa):
            inq = [False for _ in range(numSlots + N + 2)]
            q = [src]
            while len(q) > 0:
                cur = q.pop()
                inq[cur] = False
                for nei in g[cur]:
                    if capa[cur][nei] == 0:
                        continue
                    if d[nei] > d[cur] + cost[cur][nei]:
                        d[nei] = d[cur] + cost[cur][nei]
                        fa[nei] = cur
                        if not inq[nei]:
                            q.append(nei)
                            inq[nei] = True

        ans = 0

        while True:
            dist = [0x3f3f3f3f for _ in range(numSlots + N + 2)]
            pa = [-1 for _ in range(numSlots + N + 2)]
            dist[src] = 0
            spfa(dist, pa)

            if dist[dst] == 0:
                break
            mflow = 0x3f3f3f3f
            v = dst
            while v != src:
                mflow = min(mflow, capa[pa[v]][v])
                v = pa[v]
            v = dst

            while v != src:
                capa[pa[v]][v] -= mflow
                capa[v][pa[v]] += mflow
                v = pa[v]
            ans -= dist[dst] * mflow
        
        return ans


s = Solution()
s.maximumANDSum([14, 7, 9, 8, 2, 4, 11, 1, 9], 8)
