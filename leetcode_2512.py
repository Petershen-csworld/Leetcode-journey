class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        pset = set()
        nset = set()
        for p in positive_feedback:
            pset.add(p)
        for n in negative_feedback:
            nset.add(n)
        arr = []
        n = len(student_id)
        for i in range(n):
            l = report[i].split(" ")
            grades = 0
            for word in l:
                if word in pset:
                    grades += 3
                if word in nset:
                    grades -= 1
            arr.append([grades,student_id[i]])
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res
s = Solution()
s.topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2)
