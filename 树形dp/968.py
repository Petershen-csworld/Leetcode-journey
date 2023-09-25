
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def minCameraCover(self, root) -> int:
        def dfs(cur):
            if cur is None:
                return 0x3f3f3f3f ,0 ,0
            fromfa1,fromch1,choose1 = dfs(cur.left)
            fromfa2,fromch2,choose2 = dfs(cur.right)
            fromfa = min(fromch1,choose1) + min(fromch2,choose2)
            fromch = fromfa + max(0,min(choose2 - fromch2,choose1 - fromch1))
            ch = min(fromfa1,choose1)  + min(fromfa2,choose2)+ 1
            return fromfa,fromch,ch
        fromfa,fromch,ch = dfs(root)
        return min(fromch,ch)

