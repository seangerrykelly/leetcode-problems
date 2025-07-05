# https://leetcode.com/problems/capitalize-the-title/description/
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()

        for i in range(len(words)):
            if len(words[i]) > 2:
                words[i] = words[i].title()
            else:
                words[i] = words[i].lower()
        
        return " ".join(words)