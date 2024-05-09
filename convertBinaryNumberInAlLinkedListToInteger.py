# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedList(self, head):
        if head is None or head.next is None:
            return head
        
        nextNode = head.next
        previousNode = head
        head.next = None
        head = nextNode
        
        while True:
            if head.next is None:
                head.next = previousNode
                break
            nextNode = head.next
            head.next = previousNode
            previousNode = head
            head = nextNode
            
        return head

    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        reversedHead = self.reverseLinkedList(head)
        currPower = 0
        intResult = 0

        while reversedHead is not None:
            value = reversedHead.val
            intResult += value * 2**currPower
            currPower += 1
            reversedHead = reversedHead.next
        
        return intResult
        