from collections import defaultdict


class Solution(object):
    def minimumCost(self, cost, roads):
        """
        :type cost: List[int]
        :type roads: List[List[int]]
        :rtype: int
        """
        n = len(cost)
        g = defaultdict(list)

        cnt = 0
        num = 0
        count = defaultdict(list)
        st = []
        low = [0 for _ in range(n)]
        dfn = [0 for _ in range(n)]
        is_cut = [False for _ in range(n)]
        vec = []
        for a,b in roads:
            g[a].append(b)
            g[b].append(a)
        def tarjan(x):
            global cnt
            global low
            global dfn
            global num
            cnt += 1
            low[x] = dfn[x] = cnt
            flag =  0
            st.append(x)
            for nei in g[x]:
                if dfn[nei] == 0:
                    tarjan(nei)
                    low[x] = min(low[x],low[nei])
                    if low[nei] >= low[x]:
                        flag += 1
                        num += 1
                        if x != 0 or flag > 1:
                            is_cut[x] = True
                        while True:
                            cur = st.pop()
                            count[num].append(cur)
                            if cur == nei:
                                break
                        count[num].append(cur)
                else:
                    low[x] = min(low[x],dfn[nei])

        if num == 1:
            ans = 0x3f3f3f3f
            for x in  cost:
                ans = min(x,ans)
            return ans
        for i in range(1,num + 1):
            ct = 0
            mn = 0x3f3f3f3f
            for x in count[i]:
                if is_cut[x]:
                    ct += 1
                else:
                    mn = min(mn,cost[x])
            if ct == 1:
                vec.append(mn)
        vec.sort()
        ans = 0
        for i in range(len(vec) - 1):
            ans += vec[i]
        return ans
