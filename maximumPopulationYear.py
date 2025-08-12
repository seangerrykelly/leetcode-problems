# https://leetcode.com/problems/maximum-population-year/description/
class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        yearMap = {}
        maxYear = 0

        for i in range(len(logs)):
            birth, death = logs[i]
            if maxYear == 0:
                maxYear = birth
            for year in range(birth, death):
                if year not in yearMap:
                    yearMap[year] = 1
                else:
                    yearMap[year] += 1
                
                if yearMap[year] > yearMap[maxYear]:
                    maxYear = year
                    
        maxPopulation = yearMap[maxYear]
        for year in yearMap:
            if yearMap[year] == maxPopulation and year < maxYear:
                maxYear = year
        
        return maxYear