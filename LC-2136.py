class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        n = len(plantTime)
        for i in range(n):
            plantTime[i].append(growTime[i])
        plantTime.sort()
