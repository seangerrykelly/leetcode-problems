# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/?envType=daily-question&envId=2024-08-12
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.stream = nums
        self.k = k
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.stream.append(val)
        self.stream.sort(reverse=True)
        
        return self.stream[self.k - 1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)