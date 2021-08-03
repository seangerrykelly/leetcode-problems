# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        if root is None:
            return []
        
        stack = [(root, str(root.val))]
        treePaths = []
        first = True
        
        while stack:
            currNode, currPath = stack.pop()
            if first is True:
                currPath = str(currNode.val)
                first = False
            else:
                currPath = currPath + "->" + str(currNode.val)
                
            if currNode.left is not None:
                stack.append((currNode.left, currPath))
            if currNode.right is not None:
                stack.append((currNode.right, currPath))
            
            if currNode.left is None and currNode.right is None:
                treePaths.append(currPath)
        
        return treePaths