# https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12
class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        evens = []
        numMap = {}

        # Build map of digits pointing to their count
        for digit in digits:
            if str(digit) not in numMap:
                numMap[str(digit)] = 1
            else:
                numMap[str(digit)] += 1
        
        # Check every even num from 100 to 1000 and compare with map
        for i in range(100, 1000):
            if i % 2 != 0:
                continue

            num = str(i)
            currMap = {}
            for digit in num:
                if digit not in currMap:
                    currMap[digit] = 1
                else:
                    currMap[digit] += 1

            isPossible = True
            for digit in currMap:
                if digit not in numMap or numMap[digit] < currMap[digit]:
                    isPossible = False
            
            if isPossible:
                evens.append(i)
        
        return evens
        