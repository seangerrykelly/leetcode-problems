# https://leetcode.com/problems/xor-queries-of-a-subarray/description/
class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        xor = []
        answer = []

        for i in range(len(arr)):
            if i == 0:
                xor.append(arr[i])
            else:
                xor.append(xor[i-1] ^ arr[i])
        
        for query in queries:
            left, right = query
            if left == 0:
                answer.append(xor[right])
            else:
                answer.append(xor[right] ^ xor[left-1])
        
        return answer
            