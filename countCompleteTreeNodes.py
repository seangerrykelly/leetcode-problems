# https://leetcode.com/problems/count-complete-tree-nodes/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeCount = 0
        queue = [root]

        while queue:
            curr = queue.pop(0)
            if curr is None:
                continue
            nodeCount += 1
            queue.append(curr.left)
            queue.append(curr.right)
        
        return nodeCount
        