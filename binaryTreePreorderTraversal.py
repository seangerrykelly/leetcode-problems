# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        # Do recursive depth-first search
        def dfs(node):
            if node is None:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return result