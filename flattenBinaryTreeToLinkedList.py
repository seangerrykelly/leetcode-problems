# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # First, get preorder traversal of the tree
        preorder = []

        # Do recursive depth-first search
        def dfs(node):
            if node is None:
                return
            preorder.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        if len(preorder) < 2:
            return

        curr = root
        for i in range(1, len(preorder)):
            curr.right = TreeNode(preorder[i])
            curr.left = None
            curr = curr.right