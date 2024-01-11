# https://leetcode.com/problems/convert-the-temperature/
class Solution(object):
    def celsiusToKelvin(self, celsius):
        return celsius + 273.15
    
    def celsiusToFahrenheit(self, celsius):
        return celsius * 1.8 + 32.00

    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [self.celsiusToKelvin(celsius), self.celsiusToFahrenheit(celsius)]
