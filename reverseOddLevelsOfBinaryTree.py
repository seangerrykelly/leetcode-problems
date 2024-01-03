# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        levelMap = {}

        # Traverse the tree and make lists of values at odd levels
        def buildLevelMap(node, level):
            if node is None:
                return
            
            if level % 2 != 0:
                if level not in levelMap:
                    levelMap[level] = []
                levelMap[level].append(node.val)
            buildLevelMap(node.left, level + 1)
            buildLevelMap(node.right, level + 1)
        
        # Traverse tree in same order as above, and update values going through the levelMap[level] backwards
        def updateOddLevels(node, level):
            if node is None:
                return
            if level in levelMap:
                val = levelMap[level].pop()
                node.val = val
            updateOddLevels(node.left, level + 1)
            updateOddLevels(node.right, level + 1)

        buildLevelMap(root, 0)
        updateOddLevels(root, 0)
        return root
