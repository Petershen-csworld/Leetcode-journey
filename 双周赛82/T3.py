from heapq import *
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        n = len(nums1)
        diff = [0 for _ in range(n)]
        for i in range(n):
            diff[i] = -abs(nums1[i] - nums2[i])
        tot = k1 + k2
        if tot >= -sum(diff):
            return 0
        heapify(diff)
        for i in range(tot):
          cur = -heappop(diff)
          heappush(diff, 1 - cur)
        return sum(item * item for item in diff)
s = Solution()
s.minSumSquareDiff(nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1)