
class Solution(object):
        def minDiffInBST(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """

            mi = 0x3f3f3f3f
            def dfs(cur,pre):
                nonlocal mi
                if cur is None:
                    return
                dfs(cur.left,pre)
                if pre == -1:
                    pre = cur.val
                else:
                    mi = min(mi,cur.val - pre)
                    pre = cur.val
                dfs(cur.right,pre)
                return
            dfs(root,-1)
            return mi