# https://leetcode.com/problems/reverse-string/description/?envType=daily-question&envId=2024-06-02
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            start, end = s[left], s[right]
            s[left] = end
            s[right] = start
            left += 1
            right -= 1