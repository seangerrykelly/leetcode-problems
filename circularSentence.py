# https://leetcode.com/problems/circular-sentence/description/?envType=daily-question&envId=2024-11-02
class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        isCircular = True
        words = sentence.split()

        for i in range(len(words)):
            curr = words[i]
            if i == len(words) - 1:
                if curr[-1] != words[0][0]:
                    isCircular = False
                    break
            if i == 0:
                continue
            if curr[0] != words[i-1][-1]:
                isCircular = False
                break
        
        return isCircular