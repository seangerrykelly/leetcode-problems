# https://leetcode.com/problems/corporate-flight-bookings/description/
import numpy as np

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        answer = np.array([0 for i in range(n + 1)])

        # Update all items in the range instead of one at a time
        for booking in bookings:
            first, last, seats = booking
            answer[first:last+1] += seats

        reservations = answer.tolist()
        reservations.pop(0)

        return reservations