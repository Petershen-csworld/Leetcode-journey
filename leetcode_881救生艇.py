class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(people)
        people.sort()
        ###雙指針
        ###左:l 右:r
        ###p[l] + p[r] > limit
        ###r 向左移動，因爲左邊不可能再有p[l] 還比 p[l]更小了
        l, r = 0,n - 1
        tot = 0
        while l < r:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            tot += 1
        print(tot)