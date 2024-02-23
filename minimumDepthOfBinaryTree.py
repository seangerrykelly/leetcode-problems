# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bfs(self, root): 
        if root is None:
            return (root, 0)

        depth = 1
        queue = [(root, depth)]

        while queue:
            currNode, currDepth = queue.pop(0)

            if currNode.left is None and currNode.right is None:
                # This is the node we want. Keyword is MINIMUM depth
                return (currNode, currDepth)

            if currNode.left:
                queue.append((currNode.left, currDepth + 1))
            if currNode.right:
                queue.append((currNode.right, currDepth + 1))
        
        return result




    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self.bfs(root)

        return result[1]
