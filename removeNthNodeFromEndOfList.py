# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        currNode = head

        while currNode is not None:
            count += 1
            currNode = currNode.next
        
        currNode = head
        recount = 0

        # First node gets removed
        if recount == count - n:
            head = head.next
            return head

        # Any other node but the first gets removed
        while recount != count - n:
            recount += 1
            if recount == count - n:
                nextNode = currNode.next
                if nextNode.next is None:
                    currNode.next = None
                else:
                    currNode.next = nextNode.next
            currNode = currNode.next

        return head

        