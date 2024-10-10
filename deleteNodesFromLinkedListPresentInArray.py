# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2024-09-06
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        numMap = {nums[i]: True for i in range(len(nums))}

        clone = head
        prevNode = None

        while clone is not None:
            if clone.val not in numMap:
                prevNode = clone
                clone = clone.next
            else:
                # Check if the first node is being removed
                if prevNode is None:
                    clone = clone.next
                    head = clone
                    continue
                prevNode.next = clone.next
                clone = clone.next
        
        return head


