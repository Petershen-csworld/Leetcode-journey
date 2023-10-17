from collections import defaultdict


class Solution(object):
    def countVisitedNodes(self, edges):
        """
        :type edges: List[int]
        :rtype: List[int]
        """
        #### 有向缩点后 -> DAG
        n = len(edges)
        c = [0 for _ in range(n)]
        low = [0 for _ in range(n)]
        dfn = [0 for _ in range(n)]
        cnt = 0
        scc = 0
        st = []
        onstack = [False for _ in range(n)]
        count = defaultdict(int)

        def tarjan(x):
            nonlocal cnt, low, dfn, st, onstack, scc
            cnt += 1
            low[x] = dfn[x] = cnt
            nei = edges[x]
            st.append(x)
            onstack[x] = True
            if dfn[nei] == 0:
                tarjan(nei)
                low[x] = min(low[x], low[nei])
            elif onstack[nei]:
                low[x] = min(low[x], dfn[nei])
            if dfn[x] == low[x]:
                scc += 1
                flag = 0
                while True:
                    cur = st.pop()
                    onstack[cur] = False
                    flag += 1
                    c[cur] = scc
                    if cur == x:
                        break
                count[scc] = flag

        for i in range(n):
            if dfn[i] == 0:
                tarjan(i)
        g = defaultdict(list)

        ans = [0 for _ in range(scc + 1)]
        for u in range(n):
            v = edges[u]
            if c[u] != c[v]:
                g[c[u]].append(c[v])


        def dfs(cur):
            if ans[cur] != 0:
                return ans[cur]
            res = count[cur]
            for nei in g[cur]:
                res += dfs(nei)
            ans[cur] = res
            return res
        res = []
        for i in range(n):
            res.append(dfs(c[i]))
        return res

s = Solution()
s.countVisitedNodes([1,2,3,4,0])
