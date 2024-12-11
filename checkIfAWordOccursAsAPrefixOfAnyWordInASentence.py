# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/?envType=daily-question&envId=2024-12-02
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        index = -1
        words = sentence.split()

        for i in range(len(words)):
            word = words[i]
            if len(word) < len(searchWord):
                continue
            prefix = word[:len(searchWord)]
            if prefix == searchWord:
                index = i + 1 # 1-indexed array
                break
        
        return index
