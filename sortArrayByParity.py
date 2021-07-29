class Solution(object):
    
    def quick_sort(self,sequence):
        length = len(sequence)
        if length <= 1:
            return sequence
            
        even_items = []
        odd_items = []
        
        for item in sequence:
            if item % 2 == 0:
                even_items.append(item)
            else:
                odd_items.append(item)
                
        return even_items + odd_items
    
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.quick_sort(nums)
        
        