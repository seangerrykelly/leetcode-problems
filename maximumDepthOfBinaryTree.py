# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        depths = []
        
        def dfs(node, depth):
            if node is None:
                return
            newDepth = depth + 1
            if node.left is None and node.right is None:
                depths.append(newDepth)
                return
            else:
                dfs(node.left, newDepth)
                dfs(node.right, newDepth)
        
        dfs(root, 0)
        depths.sort()
        return depths[-1]