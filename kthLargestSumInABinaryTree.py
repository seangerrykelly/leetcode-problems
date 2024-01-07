# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        levelSums = {}
        
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr.pop()
            lower, greater = [], []
            for num in arr:
                if num <= pivot:
                    lower.append(num)
                else:
                    greater.append(num)
            return quickSort(greater) + [pivot] + quickSort(lower)
        
        def checkNode(node, level):
            if node is None:
                return
            if level not in levelSums:
                levelSums[level] = node.val
            else:
                levelSums[level] += node.val
            checkNode(node.left, level + 1)
            checkNode(node.right, level + 1)
        
        checkNode(root, 1)
        if k > len(levelSums):
            return -1
        
        sums = []
        for level in levelSums:
            sums.append(levelSums[level])
        
        return quickSort(sums)[k-1]
            