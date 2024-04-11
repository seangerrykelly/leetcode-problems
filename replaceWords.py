# https://leetcode.com/problems/replace-words/description/
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dictMap = {}
        result = []
        words = sentence.split()

        for word in dictionary:
            dictMap[word] = 1

        for word in words:
            root = ""
            for i in range(len(word)):
                root = word[0:i+1]
                if root in dictMap:
                    result.append(root)
                    root = ""
                    break
            
            if len(root) != 0:
                result.append(word)

        return ' '.join(result)
        