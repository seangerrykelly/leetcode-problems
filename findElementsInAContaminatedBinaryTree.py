# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.elementMap = {}
        def checkNode(node):
            if node is None:
                return
            x = node.val
            if node.left is not None:
                node.left.val = 2 * x + 1
                self.elementMap[node.left.val] = 1
            if node.right is not None:
                node.right.val = 2 * x + 2
                self.elementMap[node.right.val] = 1
            checkNode(node.left)
            checkNode(node.right)
        root.val = 0
        self.elementMap[root.val] = 1
        checkNode(root)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.elementMap
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)