# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        stack = []
        maxPairSum = 0

        while head is not None:
            stack.append(head.val)
            head = head.next

        while stack:
            twin1 = stack.pop(0)
            twin2 = stack.pop()
            pairSum = twin1 + twin2
            if pairSum > maxPairSum:
                maxPairSum = pairSum
        
        return maxPairSum
        