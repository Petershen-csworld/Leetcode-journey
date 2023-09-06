class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 1
        def dfs(cur,l):
            nonlocal ans
            ##以當前節點為末尾的串
            if cur is None:
                return -1
            ans = max(ans,l)
            if cur.left is not None:
               dfs(cur.left, l + 1 if cur.left.val == cur.val else 1)
            if cur.right is not None:
               dfs(cur.right, l + 1 if cur.right.val == cur.val else 1)
        return ans

