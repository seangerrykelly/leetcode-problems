# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/?envType=daily-question&envId=2024-03-26
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        modeMap = {}
        result = []
        stack = [root]
        mode = None

        while stack:
            curr = stack.pop()
            if curr is None:
                continue
            
            if curr.val not in modeMap:
                modeMap[curr.val] = 1
                if mode is None:
                    mode = curr.val
            else:
                modeMap[curr.val] += 1
                if modeMap[curr.val] > modeMap[mode]:
                    mode = curr.val
            
            stack.append(curr.left)
            stack.append(curr.right)
        
        for num in modeMap:
            if modeMap[num] == modeMap[mode]:
                result.append(num)

        return result