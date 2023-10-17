class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ori = ""
        for s in strs:
            ori += s + "$"
        ans = []

        def all_str(a):
            nonlocal ans
            l = len(a)
            for i in range(l):
                for j in range(i + 1, l + 1):
                    if a[i:j] is not None:
                        ans.append(a[i:j])

        for s in strs:
            all_str(s)
        m = -1
        for n in ans:
            if ori.count(n) == 1:
                m = max(m, len(n))
        return m
