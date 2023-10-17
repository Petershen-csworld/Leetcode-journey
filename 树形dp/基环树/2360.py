class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        ### 内向基环树
        n = len(edges)
        low = [0 for _ in range(n)]
        dfn = [0 for _ in range(n)]
        cnt = 0
        onstack = [False for _ in range(n)]
        scc = 0
        l = []
        msize = 0
        def tarjan(x):
            nonlocal cnt,scc,l,msize
            low[x] = dfn[x] = cnt + 1
            cnt += 1
            nei = edges[x]
            if nei == -1:
                return
            l.append(x)
            onstack[x] = True
            if dfn[nei] == 0:
                tarjan(nei)
                low[x] = min(low[x],low[nei])
            elif onstack[nei]:
                low[x] = min(low[x],dfn[nei])
            if low[x] == dfn[x]:
                scc += 1
                flag = 0
                while True:
                    cur = l.pop()
                    onstack[cur] = False
                    flag += 1
                    if cur == x:
                        break
                msize = max(msize,flag)
        for i in range(n):
            if dfn[i] == 0:
                tarjan(i)

        return msize if msize > 1 else -1

s = Solution()
s.longestCycle(edges = [2,-1,3,1])