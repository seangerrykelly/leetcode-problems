# https://leetcode.com/problems/merge-strings-alternately/description/
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        arr = ["" for i in range(len(word1) + len(word2))]
        first, second = 0, 0

        for i in range(len(arr)):
            if i % 2 == 0:
                if first < len(word1):
                    arr[i] = word1[first]
                    first += 1
                else:
                    arr[i] = word2[second]
                    second += 1
            else:
                if second < len(word2):
                    arr[i] = word2[second]
                    second += 1
                else:
                    arr[i] = word1[first]
                    first += 1
        
        return "".join(arr)

        