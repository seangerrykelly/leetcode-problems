# https://leetcode.com/problems/boats-to-save-people/description/?envType=daily-question&envId=2024-05-04
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boatCount = 0

        while people:
            if len(people) == 1:
                boatCount += 1
                break
            lightPerson, heavyPerson = people.pop(0), people.pop()
            totalWeight = lightPerson + heavyPerson
            if totalWeight <= limit:
                boatCount += 1
            else:
                boatCount += 1
                people = [lightPerson] + people

        return boatCount 