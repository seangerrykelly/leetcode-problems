# https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        number = 0
        result = []

        for digit in digits:
            number += digit*10**n
            n -= 1

        number += 1
        numString = str(number)
        
        for character in numString:
            result.append(int(character))
        
        return result
