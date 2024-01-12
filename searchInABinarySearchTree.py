# Definition for a binary tree node.
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        result = {}
        def checkNode(node):
            if node is None:
                return
            elif node.val == val:
                result[0] = node
                return
            checkNode(node.left)
            checkNode(node.right)
        checkNode(root)
        
        if 0 in result:
            return result[0]
        else:
            return None
        