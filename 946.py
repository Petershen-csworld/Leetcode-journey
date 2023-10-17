## find 大 小 中
## 312 sequence
###leetcode 456 132 pattern 树状数组 枚举3的位置
from collections import defaultdict


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        g = defaultdict(int)
        n = len(pushed)
        for i in range(n):
            g[pushed[i]] = i + 1
        for i in range(n):
            popped[i] = g[popped[i]]
