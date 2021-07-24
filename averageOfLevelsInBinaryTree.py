
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        def checkNode(node, level):
            if node is None:
                return
            if self.levelMap.get(level) is None:
                self.levelMap[level] = [1, node.val]
            else:
                self.levelMap[level][0] += 1
                self.levelMap[level][1] += node.val
            
            checkNode(node.left, level + 1)
            checkNode(node.right, level + 1)
        
        # The key value pairs will be key = levelNumber and value = [numberOfValues, sumOfValues]
        self.levelMap = {}
        checkNode(root, 0)
        averageOfLevels = []
        
        for key in self.levelMap:
            averageOfLevels.append(float(self.levelMap[key][1]) / (self.levelMap[key][0]))
            
        return averageOfLevels