# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        isOdd = n % 2
        halfwayPoint = n / 2
        answer = []
        curr = halfwayPoint

        for i in range(n):
            if i == halfwayPoint and isOdd:
                answer.append(0)
            else:
                if curr == 0:
                    curr -= 1
                answer.append(curr)
                curr -= 1

        return answer
            
        