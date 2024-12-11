# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        teams = []
        skill.sort()
        skillLevel = 0
        chemistry = 0

        while len(skill) > 0:
            teams.append([skill.pop(0), skill.pop()])
            currSkill = sum(teams[-1])
            if skillLevel == 0:
                skillLevel = currSkill
            elif skillLevel != currSkill:
                return -1
            
            chemistry += teams[-1][0] * teams[-1][1]
        
        return chemistry