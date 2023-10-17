class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        n = len(favorite)
        inc = [0 for _ in range(n)]
        rg = defaultdict(list)
        for i in range(n):
            inc[favorite[i]] += 1
            rg[favorite[i]].append(i)

        def topo():
            nonlocal inc
            q = []
            for i in range(n):
                if inc[i] == 0:
                    q.append(i)
            while len(q) > 0:
                cur = q.pop()
                inc[favorite[cur]] -= 1
                if inc[favorite[cur]] == 0:
                    q.append(favorite[cur])

        circ = 0
        for i in range(n):
            if inc[i] > 0:
                circ += 1
        if circ > 2:
            return circ
        ans = [0 for _ in range(n)]

        def rdfs(u):
            depth = 1
            for nei in rg[u]:
                if inc[nei] == 0:
                    depth = max(depth,rdfs(nei) + 1)
            return depth
        mring = schain = 0
        for i,d in enumerate(inc):
            if d <= 0:
                continue
            inc[i] = -1
            rsize = 1
            v = favorite[i]
            while v != i:
                inc[v] = -1
                rsize += 1
                v = favorite[v]
            if rsize == 2:
                schain += rdfs(i) + rdfs(favorite[i])
            else:
                mring = max(mring,rsize)
            return max(schain,mring)


