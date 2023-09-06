class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        cnt = 0
        while num2 != 0 and num1 != 0:

            if num1 >= num2:
                val = (num1 - num2)//num2
                num1 -= (val + 1) * num2
                cnt += val
            else:
                num2 , num1 = num1,num2

        return cnt
s = Solution()
s.countOperations(2,3)