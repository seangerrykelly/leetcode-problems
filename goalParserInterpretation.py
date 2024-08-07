# https://leetcode.com/problems/goal-parser-interpretation/description/
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack = []
        interpretation = ""
        for i in range(len(command)):
            if command[i] == '(':
                stack.append(i)
            elif command[i] == ')' and len(stack) > 0 and command[stack[-1]] == '(':
                # This is where we interpret the bracket pair
                if i - stack[-1] == 1:
                    interpretation += 'o'
                stack.pop()
            else:
                interpretation += command[i]

        return interpretation