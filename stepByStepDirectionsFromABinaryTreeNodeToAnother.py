# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/?envType=daily-question&envId=2024-07-16
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        pathToStart, pathToDest = "", ""
        stack = [(root, "")]

        while stack:
            node, currPath = stack.pop()
            if node is None:
                continue
            if node.left is not None:
                stack.append((node.left, currPath + "L"))
            if node.right is not None:
                stack.append((node.right, currPath + "R"))
            if node.val == startValue:
                pathToStart = currPath
            if node.val == destValue:
                pathToDest = currPath
        
        trimIndex = -1
        for i in range(min(len(pathToStart), len(pathToDest))):
            currStart, currDest = pathToStart[i], pathToDest[i]
            if currStart == currDest:
                trimIndex = i
            else:
                break
        
        if trimIndex != -1:
            pathToStart = pathToStart[trimIndex+1:]
            pathToDest = pathToDest[trimIndex+1:]
        
        pathToStart = "U" * len(pathToStart)

        return pathToStart + pathToDest
        