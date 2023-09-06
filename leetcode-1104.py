class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        d = 0
        l = label
        while l > 0:
            l = l // 2
            d += 1
        cur = d - 1
        while label > 0:
            res.append(label)
            if cur % 2 == 0:
                orilabel = pow(2, cur + 1) + pow(2, cur) - label - 1
                label = orilabel // 2
            else:
                orilabel = label // 2
                fake = pow(2, cur ) + pow(2, cur - 1) - orilabel - 1
                label = fake
            cur -= 1
        res.reverse()


        return res


s = Solution()
s.pathInZigZagTree(26533)
