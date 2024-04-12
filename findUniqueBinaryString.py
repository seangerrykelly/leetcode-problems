# https://leetcode.com/problems/find-unique-binary-string/description/
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        maxNumber = 2**n - 1 if n > 1 else 2
        baseTenMap = {}
        binaryString = ""

        for num in nums:
            baseTen = 0
            for i in range(n):
                digit = int(num[i])
                multiplier = 2**(n-i-1)
                baseTen += (digit * multiplier)
            baseTenMap[baseTen] = 1
                
        for i in range(maxNumber):
            if i not in baseTenMap:
                missingNumber = i
                # Convert missing number to binary string
                for j in reversed(range(n)):
                    curr = 2**j
                    if missingNumber < curr:
                        binaryString += '0'
                    elif missingNumber >= curr:
                        binaryString += '1'
                        missingNumber -= curr
                break

        return binaryString
            