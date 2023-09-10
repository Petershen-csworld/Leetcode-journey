class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ### 基於值域的 綫段樹
        class Node:
          def __init__(self):
             self.ls = None
             self.rs = None
             self.val = 0
        def update(node,lc,rc,x,val):
            if lc == rc:
                node.val = val
                return
            if node.ls is None:
                node.ls = Node()
            if node.rs is None:
                node.rs = Node()
            mid = lc + rc >> 1
            if x <= mid:
                update(node.rs,lc,mid,x,val)
            else:
                update(node.ls,mid + 1,rc,x,val)
            pushup(node)
        def query(node,lc,rc,l,r):
            if node is None:
                return 0
            if l > rc or r < lc:
                return 0

            if lc >= l and rc <= r:
                return node.val
            ma = 0
            mid = lc + rc >> 1
            if l <= mid:
                ma = max(ma,query(node.ls,lc,mid,l,r))
            if r > mid:
                ma = max(ma,query(node.rs,mid + 1,rc,l,r))
            return ma
        def pushup(node):
            node.val = max(node.ls.val,node.rs.val)
        root = Node()
        n = len(nums)
        ma = max(nums)
        res = 1
        update(root,1,ma,nums[0],1)
        for i in range(1,n):
            curmax = query(root,1,ma,max(1,nums[i] - k),nums[i] - 1)
            res = max(res,curmax + 1)
            update(root,1,ma,nums[i],res + 1)
        return res
s = Solution()
s.lengthOfLIS(nums = [1,5], k = 1)