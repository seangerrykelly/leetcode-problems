# https://leetcode.com/problems/delete-node-in-a-linked-list/description/?envType=daily-question&envId=2024-05-05
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node is not None:
            nextNode = node.next
            node.val = nextNode.val
            if node.next.next is None:
                node.next = None
                break
            node = node.next
