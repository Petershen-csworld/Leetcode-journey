class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        last = None
        a = None
        b = None
        ## Morris遍歷
        while root is not None:
            if root.left is None:
                if last is not None and last.val > root.val:
                    if a is None:
                        a = last
                        b = root
                    else:
                        b = root
                last = root
                root = root.right
            else:
                t = root.left
                while t.right is not None and t.right is not root:
                    t = t.right
                if t.right is None:
                    t.right = root
                    root = root.left
                else:
                    t.right = None
                    if last is not None and last.val > root.val:
                        if a is None:
                            a = last
                            b = root
                        else:
                            b = root
                    last = root
                    root = root.right
        val = a.val
        a.val = b.val
        b.val = val






