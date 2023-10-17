class Solution(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        dp = [[] for _ in range(n + 1)]
        m = -1
        res = []
        for i in range(1,n + 1):

            mlen = len(dp[i])
            midx = -1
            for j in range(1,i):
                if groups[i - 1] != groups[j - 1]:
                    if len(dp[j]) + 1 > mlen:
                        mlen = len(dp[j]) + 1
                        midx = j


            if midx != -1:
               dp[i] = dp[midx].copy()
            dp[i].append(words[i - 1])
            if mlen > m:
                m = max(mlen,m)
                res = dp[i]
        return res

s = Solution()
s.getWordsInLongestSubsequence(n = 4, words = ["a","b","c","d"], groups = [1,0,1,1])