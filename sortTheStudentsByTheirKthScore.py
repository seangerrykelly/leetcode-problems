# https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/
class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr.pop()
            lower, greater = [], []
            for item in arr:
                if item[1] <= pivot[1]:
                    lower.append(item)
                else:
                    greater.append(item)
            
            return quickSort(greater) + [pivot] + quickSort(lower)

        students = []
        for i in range(len(score)):
            kthScore = score[i][k]
            students.append((i,kthScore))
        
        sortedResults = []
        students = quickSort(students)
        for student in students:
            sortedResults.append(score[student[0]])

        return sortedResults