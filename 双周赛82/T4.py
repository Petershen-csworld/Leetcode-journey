class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        tr = [0x3f3f3f3f3f for _ in range(4 * pow(10, 5) + 10)]

        def build(o, lc, rc):
            if lc == rc:
                tr[o] = nums[lc]
                return
            mid = lc + rc >> 1
            build(o << 1, lc, mid)
            build(o << 1 | 1, mid + 1, rc)
            tr[o] = min(tr[o << 1], tr[o << 1 | 1])

        def query(o, lc, rc, l, r):
            if l <= lc and r >= rc:
                return tr[o]
            if l > rc or r < lc:
                return -1
            mid = lc + rc >> 1
            ans = 0x3f3f3f3f3f3f
            if l <= mid:
                ans = min(ans, query(o << 1, lc, mid, l, r))
            if r > mid:
                ans = min(ans, query(o << 1 | 1, mid + 1, rc, l, r))
            return ans

        build(1, 0, n - 1)

        def check(le):
            for i in range(n - le + 1):
                end = i + le - 1
                rmq = query(1, 0, n - 1, i, end)
                if rmq > threshold / le:
                    return True
            return False

        left = 1
        right = n + 1
        res = 0x3f3f3f3f
        while left < right:
            mid = (left + right ) >> 1
            print(mid)
            print(check(mid))
            if check(mid):
                res = min(res, mid)
                right = mid
            else:
                left = mid + 1
        print(check(9))
        print(res)
        return res if res != 0x3f3f3f3f else -1



s = Solution()
s.validSubarraySize([373,466,501,884,998,254,12,324,813,601,790,728,754,676,958,505,317,117,727,2,248,305,481,12,394,282,173,623,841,636,500,234,524,501,694,506,312,723,801],2228)
