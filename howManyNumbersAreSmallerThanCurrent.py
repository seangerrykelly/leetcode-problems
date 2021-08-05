class Solution(object):
    
    def quick_sort(self, array):
        
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()
            
        itemsLower, itemsGreater = [],[]
        
        for item in array:
            if item > pivot:
                itemsGreater.append(item)
            else:
                itemsLower.append(item)
                
        return self.quick_sort(itemsGreater) + [pivot] + self.quick_sort(itemsLower)
    
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        descendingNums = self.quick_sort(list(nums))
        smallerNumbersMap = {}
        counter = len(nums) - 1
        numberCounts = []
        
        for i in descendingNums:
            smallerNumbersMap[i] = counter
            counter -= 1
        
        for i in nums:
            numberCounts.append(smallerNumbersMap[i])
            
        return numberCounts