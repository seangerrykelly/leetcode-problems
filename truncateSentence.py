# https://leetcode.com/problems/truncate-sentence/description/
class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words = s.split()
        words = words[:k]
        truncatedSentence = ""
        
        for i in range(len(words)):
            if i == len(words) - 1:
                truncatedSentence += words[i]
            else:
                truncatedSentence += words[i] + ' '

        return truncatedSentence