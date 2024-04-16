# https://leetcode.com/problems/add-one-row-to-tree/description/?envType=daily-question&envId=2024-04-16
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        # Edge case of depth == 1
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        # Need to keep track of current node, depth, parent node, and if left or right
        queue = [(root, 1, None, False)]
        
        # Use breadth first search to traverse level by level
        while queue:
            currNode, currDepth, parentNode, isLeft = queue.pop(0)

            if currNode is None:
                # If the desired depth is one level deeper than leaf node
                if currDepth == depth:
                    if isLeft:
                        parentNode.left = TreeNode(val)
                    else:
                        parentNode.right = TreeNode(val)
                continue
            if currDepth == depth:
                subtreeRoot = TreeNode(val)
                if isLeft:
                    parentNode.left = subtreeRoot
                    subtreeRoot.left = currNode
                else:
                    parentNode.right = subtreeRoot
                    subtreeRoot.right = currNode
            
            queue.append((currNode.left, currDepth + 1, currNode, True))
            queue.append((currNode.right, currDepth + 1, currNode, False))

        return root
            