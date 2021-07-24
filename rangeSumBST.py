# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inRange(self, value, low, high):
        return (value >= low and value <= high)
    
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        def depthFirstSearch(treeNode):
            if treeNode is None:
                return
            if self.inRange(treeNode.val, low, high):
                self.out += treeNode.val
            if treeNode.val > low:
                depthFirstSearch(treeNode.left)
            if treeNode.val < high:
                depthFirstSearch(treeNode.right)
            
        self.out = 0
        depthFirstSearch(root)
        return self.out