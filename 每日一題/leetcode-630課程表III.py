import heapq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses = sorted(courses,key = lambda x: x[1])
        q = []
        n = len(courses)
        cursum = 0
        for duration, lastday in courses:
            if cursum + duration <= lastday:
                cursum += duration
                heapq.heappush(q,-cursum)
            elif q and duration < -q[0]:
                cursum -= -heapq.heapreplace(q,-duration) - duration
        return len(q)
