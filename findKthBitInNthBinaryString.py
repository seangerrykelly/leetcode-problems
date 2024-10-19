# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=daily-question&envId=2024-10-19
class Solution(object):
    def invertBinaryString(self, b):
        bitCount = len(b)
        num = int(b, 2)
        invertedNum = ~num
        
        mask = (1 << bitCount) - 1
        answer = invertedNum & mask
        invertedBinaryString = bin(answer)[2:].zfill(bitCount)

        return invertedBinaryString
    
    def reverseString(self, s):
        reversedStr = s[::-1]
        return reversedStr

    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s = "0"
        for i in range(1, n):
            s += "1" + self.reverseString(self.invertBinaryString(s))
            if len(s) >= k:
                break

        return s[k-1]