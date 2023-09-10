class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left is None and root.right is None:
            return True if root.val == 1 else False
        lval = self.evaluateTree(root.left)
        rval = self.evaluateTree(root.right)
        return lval | rval if root.val == 2 else lval & rval