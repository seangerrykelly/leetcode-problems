# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def invertNode(node):
            if node is None:
                return
            else:
                clone = node.left
                node.left = node.right
                node.right = clone
                invertNode(node.left)
                invertNode(node.right)
        
        invertNode(root)
        return root
        