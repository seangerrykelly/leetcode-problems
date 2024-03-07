# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [(root, 0)]
        nodeMap = {}

        while queue:
            currNode, currLevel = queue.pop(0)
            if currNode is None:
                continue
            if currLevel not in nodeMap:
                nodeMap[currLevel] = [currNode.val]
            else:
                nodeMap[currLevel].append(currNode.val)
            queue.append((currNode.left, currLevel + 1))
            queue.append((currNode.right, currLevel + 1))
        
        result = nodeMap.values()
        return result