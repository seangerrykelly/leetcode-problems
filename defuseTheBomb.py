# https://leetcode.com/problems/defuse-the-bomb/description/?envType=daily-question&envId=2024-11-18
# Ended up brute forcing this one so it's not my best work
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        decoded = []
        n = len(code)
        code += code
        i = n if k < 0 else 0
        curr = 0
        currSum = 0
        prev = None
        
        if k > 0:
            for i in range(i, i+n):
                for j in range(k):
                    prev = code[i+j+1]
                    currSum += prev
                decoded.append(currSum)
                currSum = 0
                curr += 1
        elif k < 0:
            for i in reversed(range(i)):
                for j in range(abs(k)):
                    prev = code[i-j-1]
                    currSum += prev
                decoded.append(currSum)
                currSum = 0
                curr += 1
            decoded.reverse()
        else:
            decoded = [0 for i in range(n)]
        
        return decoded
        
        