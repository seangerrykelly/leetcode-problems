# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=daily-question&envId=2024-03-07
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        node = head

        while node is not None:
            count += 1
            node = node.next

        isEven = count % 2 == 0
        middle = count / 2
    
        for i in range(middle):
            head = head.next
        
        return head
        