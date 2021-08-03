class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ipSegments = address.split('.')
        defangedIP = ""
        for i in range(len(ipSegments)):
            if i == len(ipSegments) - 1:
                defangedIP += ipSegments[i]
                break
            else:
                defangedIP += ipSegments[i] + "[.]"
        return defangedIP