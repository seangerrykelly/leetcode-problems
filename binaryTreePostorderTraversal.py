# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal = []
        def postorder(node):
            if node is not None:
                if node.left is None and node.right is None:
                    traversal.append(node.val)
                else:
                    if node.left is not None:
                        traversal.append(postorder(node.left))
                    if node.right is not None:
                        traversal.append(postorder(node.right))
                    traversal.append(node.val)
        
        postorder(root)
        traversal = [x for x in traversal if x is not None]

        return traversal
        