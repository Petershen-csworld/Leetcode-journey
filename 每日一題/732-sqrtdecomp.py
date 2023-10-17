from collections import defaultdict


class MyCalendarThree(object):

    def __init__(self):
        self.Max = [0 for _ in range(32000)]
        self.SZ = 32000
        self.g = defaultdict(int)
        self.lazy = [0 for _ in range(32000)]

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: int
        """

        def add(i, j, val):
            lidx = (i - 1) // self.SZ + 1
            ridx = (j - 1) // self.SZ + 1
            if lidx == ridx:
                for k in range(i, j + 1):
                    self.g[k] += val
            lbound = lidx * self.SZ
            rbound = (ridx - 1) * self.SZ + 1
            for l in range(i, lbound + 1):
                self.g[l] += val
                if self.g[l] > self.Max[lidx]:
                    self.Max[lidx] = self.g[l]
            for l in range(rbound, j + 1):
                self.g[l] += val
                if self.g[l] > self.Max[ridx]:
                    self.Max[ridx] = self.g[l]
            for l in range(lidx + 1, ridx):
                self.lazy[l] += val

        def query(i, j):
            lidx = (i - 1) // self.SZ + 1
            ridx = (j - 1) // self.SZ + 1
            res = 0
            if lidx == ridx:
                for l in range(i, j + 1):
                    res = max(res, self.g[l] + self.lazy[l])
            lbound = lidx * self.SZ
            rbound = (ridx - 1) * self.SZ + 1
            for l in range(i, lbound + 1):
                res = max(res, self.g[l] + self.lazy[lidx])
            for l in range(rbound ,j + 1):
                res = max(res, self.g[l] + self.lazy[lidx])
            for l in range(lidx + 1, ridx):
                res = max(res, self.g[l] + self.lazy[l])

        add(startTime, endTime - 1, 1)
        return query(startTime, endTime - 1)
