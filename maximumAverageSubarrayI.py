class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        averages = []
        currSum = 0.0
        currK = 0

        for i in range(len(nums)):
            if currK < k:
                # Count k elements
                currK += 1
                currSum += nums[i]
            else:
                # Use prefix sum methods to track currSum
                currSum -= nums[i-k]
                currSum += nums[i]
            
            if currK == k:
                # Calculate average
                averages.append(currSum / k)
        
        return max(averages)
            