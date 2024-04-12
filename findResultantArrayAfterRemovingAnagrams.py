# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/
class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        prevAnagram = {}
        result = []

        for word in words:
            letterMap = {}
            for letter in word:
                if letter not in letterMap:
                    letterMap[letter] = 1
                else:
                    letterMap[letter] += 1
            

            if prevAnagram == letterMap:
                continue
            elif len(prevAnagram) == 0 or prevAnagram != letterMap:
                prevAnagram = letterMap
                result.append(word)

        return result
