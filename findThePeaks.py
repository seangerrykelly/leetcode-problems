# https://leetcode.com/problems/find-the-peaks/description/
class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        peaks = []
        for i in range(1, len(mountain)-1):
            mPrev = mountain[i-1]
            mCurr = mountain[i]
            mNext = mountain[i+1]
            if mCurr > mPrev and mCurr > mNext:
                peaks.append(i)
        
        return peaks