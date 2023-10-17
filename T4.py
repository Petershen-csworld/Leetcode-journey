from collections import defaultdict


class Solution(object):
    def countSubMultisets(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """

        MOD = pow(10, 9) + 7
        n = len(nums)
        dp1 = [0 for _ in range(r + 1)]
        res = 0
        dp1[0] = 1
        for i in range(n):
            for j in range(r,nums[i] - 1, -1):
                    dp1[j] = (dp1[j] + dp1[j - nums[i]]) % MOD
        for i in range(l,r + 1):
            res += dp1[i]
        print(res)
        print(dp1)
        return res




    def countSubMultisets1(self, nums, l, r):
            """
            :type nums: List[int]
            :type l: int
            :type r: int
            :rtype: int
            """
            g = defaultdict(int)
            for num in nums:
                g[num] += 1
            newnum = [[] for _ in range(len(g.keys()))]
            i = 0
            for n in g.keys():
                for k in range(1, g[n] + 1):
                    newnum[i].append(n * k)
                i += 1
            MOD = pow(10, 9) + 7
            n = len(newnum)
            dp1 = [0 for _ in range(r + 1)]
            dp1[0] = 1
            res = 0
            for i in range(n):
                for j in range(r,-1,-1):
                    for k in newnum[i]:
                        if j >= k:
                          dp1[j] = (dp1[j] + dp1[j - k]) % MOD

            for i in range(l, r + 1):
                res += dp1[i]
            print(dp1 )

            return res


s = Solution()
s.countSubMultisets1([0,0,1,2,3],2,3)
