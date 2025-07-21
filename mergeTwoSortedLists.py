# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None

        nums = []
        while list1 is not None:
            nums.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            nums.append(list2.val)
            list2 = list2.next
        nums.sort()
        head = ListNode(nums[0])
        curr = head

        for i in range(len(nums)):
            if curr is None:
                curr = ListNode(nums[i])
            else:
                curr.val = nums[i]
            if i != len(nums) - 1:
                curr.next = ListNode()
            curr = curr.next
            
        return head
        