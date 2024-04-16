class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = str(x)[::-1]
        maximum = (2**31) - 1

        if x < 0:
            reverse = '-' + reverse[:len(reverse)-1]

        reverseInt = int(reverse)

        if abs(reverseInt) >= maximum:
            return 0
        
        return int(reverse)