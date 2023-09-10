class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
### advantage : no extra space
def morrisinorder(root):
    while root is not None:
        if root.left is None:
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
                root = root.right

s = TreeNode(3)
s.left = TreeNode(2)
morrisinorder(s)