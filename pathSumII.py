# https://leetcode.com/problems/path-sum-ii/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        paths = []
        stack = [(root, 0, [])]

        while stack:
            currNode, currSum, currPath = stack.pop()
            if currNode is None:
                continue
            
            currSum += currNode.val
            currPath.append(currNode.val)
            if currNode.left is None and currNode.right is None and currSum == targetSum:
                paths.append(currPath)
            else:
                stack.append((currNode.left, currSum, currPath[:]))
                stack.append((currNode.right, currSum, currPath[:]))
        
        return paths


        