import bisect


class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        passengers.sort()
        buses.sort()
        pre = 0
        buslen = len(buses)
        paslen = len(passengers)
        i = 0
        j = 0
        pre = 0
        group = 0
        ma = -1
        while i < buslen and j <= paslen:
            while passengers[j] <= buses[i] and j - pre < capacity:
                j += 1
            group += 1
            if group == buslen:
                break
            pre = j
            i += 1




s = Solution()
s.latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2)
