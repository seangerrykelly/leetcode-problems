# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr.pop()
            lower, greater = [], []
            for item in arr:
                if item <= pivot:
                    lower.append(item)
                else:
                    greater.append(item)
            return quickSort(lower) + [pivot] + quickSort(greater)
        
        averageSalary = 0
        sortedSalaries = quickSort(salary)
        salaryCount = len(sortedSalaries) - 2
        
        for i in range(1, len(sortedSalaries) - 1):
            averageSalary += sortedSalaries[i]
        
        return averageSalary / float(salaryCount)