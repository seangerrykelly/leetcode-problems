# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/
class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr.pop()
            lower, greater = [], []
            for num in arr:
                if num <= pivot:
                    lower.append(num)
                else:
                    greater.append(num)
            return quickSort(lower) + [pivot] + quickSort(greater)

        moveCount = 0
        seats = quickSort(seats)
        students = quickSort(students)

        for i in range(len(seats)):
            currSeat, currStudent = seats[i], students[i]
            currMoves = abs(currStudent - currSeat)
            moveCount += currMoves

        return moveCount