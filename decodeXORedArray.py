# https://leetcode.com/problems/decode-xored-array/
class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        decodedArr = [first]
        for i in range(0, len(encoded)):
            nextElement = encoded[i] ^ decodedArr[i]
            decodedArr.append(nextElement)
        
        return decodedArr