# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root):
        if root is None:
            return []
        result = []
        stack = [root]

        while stack:
            curr = stack.pop()
            result.append(curr.val)
            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return result

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeList = self.dfs(root)
        nodeList.sort()
        
        minDiff = 0
        i, j = 0, 1

        while j < len(nodeList):
            left, right = nodeList[i], nodeList[j]
            currDiff = right - left
            if i == 0 or currDiff < minDiff:
                minDiff = currDiff
            
            i += 1
            j += 1
        
        return minDiff

        