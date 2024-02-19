# https://leetcode.com/problems/find-words-containing-character/description/
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        answer = []
        for i in range(len(words)):
            curr = words[i]
            if x in curr:
                answer.append(i)
        
        return answer