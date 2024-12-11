# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/?envType=daily-question&envId=2024-12-10
class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        currSubstring = s[0]
        thriceMap = {currSubstring: [1, [currSubstring]]}
        longestLength = -1

        for i in range(1, len(s)):
            currChar = s[i]
            if currChar == currSubstring[-1]:
                currSubstring += currChar
            else:
                currSubstring = currChar
            
            if currChar not in thriceMap:
                thriceMap[currChar] = [1, [currSubstring]]
            else:
                thriceMap[currChar][0] += 1
                if currSubstring not in thriceMap[currChar][1]:
                    thriceMap[currChar][1].append(currSubstring)
        
        for letter in thriceMap:
            if thriceMap[letter][0] < 3:
                continue
            for i in range(len(thriceMap[letter][1])):
                substr = thriceMap[letter][1][i]
                currCount = 0
                for j in range(0, len(s) - len(substr) + 1):
                    comparator = s[j:j+len(substr)]
                    if comparator == substr:
                        currCount += 1
                if currCount >= 3 and len(substr) > longestLength:
                    longestLength = len(substr)
        
        return longestLength