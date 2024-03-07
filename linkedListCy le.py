# https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeMap = {}
        hasCycle = False

        while head is not None:
            if head not in nodeMap:
                nodeMap[head] = 1
            else:
                hasCycle = True
                break
            head = head.next

        return hasCycle
        