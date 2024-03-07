# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05
# This is a very messy solution. I had 99/100 test cases passing and
# just added an alternative block of code for extremely large inputs.
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] != s[-1] or len(s) == 1:
            return len(s)
        
        if len(s) >= pow(10, 4):
            left, right = 0, len(s) - 1
            prefix, suffix = "", ""
            prefixFound, suffixFound = False, False
            while s[0] == s[-1]:
                if prefixFound == False:
                    if len(prefix) == 0:
                        prefix = s[left]
                        left += 1
                    elif s[left] != prefix[0]:
                        prefixFound = True
                    else:
                        prefix += s[left]
                        left += 1

                if suffixFound == False:
                    if len(suffix) == 0:
                        suffix = s[right]
                        right -= 1
                    elif s[right] != suffix[0]:
                        suffixFound = True
                    else:
                        suffix += s[right]
                        right -= 1

                if suffixFound and prefixFound:
                    s = s[len(prefix):len(s) - len(suffix)]
                    left, right = 0, len(s) - 1
                    prefix, suffix = "", ""
                    prefixFound, suffixFound = False, False

                if len(s) <= 1:
                    break
                elif len(s) == 2:
                    if s[0] == s[-1]:
                        s = ""
                        break
        else:
            while s[0] == s[-1]:
                prefix, suffix = "", ""
                for i in range(len(s)):
                    if i == 0:
                        prefix = s[0]
                    elif s[i] != prefix[0]:
                        break
                    else:
                        prefix += s[i]
                
                for i in reversed(range(len(s))):
                    if i == len(s) - 1:
                        suffix = s[i]
                    elif s[i] != suffix[0]:
                        break
                    else:
                        suffix += s[i]
                s = s[len(prefix):len(s) - len(suffix)]
                if len(s) <= 1:
                    break

        return len(s)