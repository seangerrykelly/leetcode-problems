class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        bracketMap = { '(': ')' }
        result = ""

        start, end = 0, 0
        for bracket in s:
            if bracket in bracketMap:
                stack.append(bracket)
            else:
                if len(stack) > 0 and bracket == bracketMap[stack[-1]]:
                    stack.pop()
                
                if len(stack) == 0:
                    primitive = s[start+1:end]
                    result += primitive
                    start = end + 1
            end += 1

        return result
        