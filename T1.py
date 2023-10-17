class Solution(object):
    def lastVisitedIntegers(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        k = 0
        res = []
        ans = []
        for w in words:
            if w == "prev":
                k += 1
                if k > len(res):
                    ans.append(-1)
                else:
                    res.reverse()
                    ans.append(res[k - 1])
                    res.reverse()
            else:
                res.append(int(w))
                k = 0
        return ans
s  = Solution()
s.lastVisitedIntegers(words = ["1","prev","2","prev","prev"])