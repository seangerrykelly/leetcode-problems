# https://leetcode.com/problems/lemonade-change/?envType=daily-question&envId=2024-08-15
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changeMap = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            changeMap[bill] += 1
            if bill == 10:
                if changeMap[5] >= 1:
                    changeMap[5] -= 1
                else:
                    return False
            elif bill == 20:
                if changeMap[10] >= 1 and changeMap[5] >= 1:
                    changeMap[10] -= 1
                    changeMap[5] -= 1
                elif changeMap[10] == 0 and changeMap[5] >= 3:
                    changeMap[5] -= 3
                else:
                    return False
        return True
