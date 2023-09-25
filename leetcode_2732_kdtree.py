class Solution:
    def maximumSumQueries(self, nums1, nums2, queries):
        """
    :type nums1: List[int]
    :type nums2: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """

        class kdtree:
            def __init__(self, data):
                self.data = data
                self.ls = None
                self.rs = None

        K = 2

        def insert(o, x, depth):

            axis = depth % K
            if o.data[axis] > x[axis]:
                if o.ls:
                    insert(o.ls, x, depth + 1)
                else:
                    o.ls = kdtree(x)
            else:
                if o.rs:
                    insert(o.rs, x, depth + 1)
                else:
                    o.rs = kdtree(x)

        ans = []

        def rangequery(o, mi, ma, depth):
            if not o:
                return
            axis = depth % K
            if mi[axis] <= o.data[axis] <= ma[axis]:
                if all(mi[i] <= o.data[i] <= ma[i] for i in range(K)):
                    ans.append(o.data)
            if o.data[axis] >= mi[axis]:
                rangequery(o.ls, mi, ma, depth + 1)
            if o.data[axis] <= ma[axis]:
                rangequery(o.rs, mi, ma, depth + 1)

        root = None
        for i in range(len(nums1)):
            u, v = nums1[i], nums2[i]
            if not root:
                root = kdtree([u, v])
            else:
                insert(root, [u, v], 0)


        res = []
        for a, b in queries:
            c = -1
            rangequery(root, [a,b], [0x3f3f3f3f, 0x3f3f3f3f], 0)
            for u,v in ans:
                c = max(c,u + v)
            res.append(c)
            ans =[]

        return res


s = Solution()
s.maximumSumQueries(nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]])
