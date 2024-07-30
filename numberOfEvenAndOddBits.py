# https://leetcode.com/problems/number-of-even-and-odd-bits/description/
class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer = [0, 0]

        # Convert n to binary and reverse it
        binaryN = bin(n)[2:]
        binaryN = binaryN[::-1]
        
        for i in range(len(binaryN)):
            currBit = binaryN[i]
            if currBit == '1':
                if i % 2 == 0:
                    answer[0] += 1
                else:
                    answer[1] += 1
        
        return answer
