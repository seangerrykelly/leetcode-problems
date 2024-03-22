# https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-22
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseSequence(self, sequence):
        return sequence[::-1]

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        
        sequence = []
        while True:
            sequence.append(head.val)
            head = head.next
            if head == None:
                break
        
        return sequence == self.reverseSequence(sequence)
