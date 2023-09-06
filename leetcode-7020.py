import bisect


class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        isk = [0 for _ in range(n)]
        pre = [0 for _ in range(n + 1)]
        for i in range(n):
            isk[i] = 1 if (nums[i] % modulo) == k else 0
        for i in range(n):
            pre[i + 1] = pre[i] + isk[i]
        cnt = 0

        def find_num_of_cur(tar):
            nonlocal cnt

            for idx in range(1, n + 1):
                target = pre[idx] - tar
                if target > pre[idx] or target < 0 :
                    continue
                lmost = bisect.bisect_left(pre,target)
                rmost = bisect.bisect_right(pre,target) - 1

                ok = pre[lmost] == pre[rmost] == target and rmost >= lmost and rmost <= idx and lmost < idx
                add = 0 if not ok else (rmost - lmost + 1) if pre[rmost] != pre[idx] else rmost - lmost

                cnt += add

        for i in range(k, pre[n] - pre[0] + 1, modulo):
            find_num_of_cur(i)
        print(pre)


        return cnt


s = Solution()
s.countInterestingSubarrays([3,5,4,2],5,0)
