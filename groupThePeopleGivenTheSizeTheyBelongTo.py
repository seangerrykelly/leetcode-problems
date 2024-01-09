# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groupList = []
        sizeMap = {}

        # Map (size) -> (group) and everytime size == len(group), add group to result
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in sizeMap:
                sizeMap[size] = [i]
            else:
                sizeMap[size].append(i)

            if size == len(sizeMap[size]):
                groupList.append(sizeMap[size])
                sizeMap[size] = []
        
        return groupList