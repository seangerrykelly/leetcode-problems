# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        parent, grandparent = None, None
        evenGrandparentSum = 0
        stack = [(root, parent, grandparent)]
        grandparentMap = {}
        visitedNodes = {}
            
        while stack:
            curr, parent, grandparent = stack.pop()
            
            if curr is None:
                continue
                
            if visitedNodes.get(curr.left) is None:
                stack.append((curr.left, curr, parent))
            if visitedNodes.get(curr.right) is None:
                stack.append((curr.right, curr, parent))
            visitedNodes[curr] = True
                
            if parent is None and grandparent is None:
                parent = curr
            elif parent is not None and grandparent is None:
                grandparent = parent
                parent = curr
            else:
                grandparentMap[curr] = grandparent.val
                if grandparent.val % 2 == 0:
                    evenGrandparentSum += curr.val
                
        return evenGrandparentSum