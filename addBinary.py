class Solution(object):
    
    def binaryToBaseTen(self, binaryString):
        highestPower = len(binaryString) - 1
        num = 0
        idx = 0
        
        while highestPower >= 0:
            num += (int(binaryString[idx])) * (2**highestPower)
            highestPower -= 1
            idx += 1
        return num
    
    def baseTenToBinary(self, baseTenInt):
        highestPower = 0
        powerOfTwo = 0
        
        while True:
            minimum = 2**powerOfTwo
            maximum = 2**(powerOfTwo + 1)
            if baseTenInt >= minimum and baseTenInt < maximum:
                highestPower = minimum
                break
            powerOfTwo += 1
        
        binaryString = ""
        
        while True:
            currentSquare = 2**powerOfTwo
            powerOfTwo -= 1
        
            if baseTenInt - currentSquare >= 0:
                binaryString = binaryString + "1"
                baseTenInt -= currentSquare
            else:
                binaryString = binaryString + "0"
            
            if powerOfTwo < 0:
                break
        
        return binaryString
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if a == "0":
            return b
        if b == "0":
            return a
        
        aBaseTen, bBaseTen = self.binaryToBaseTen(a), self.binaryToBaseTen(b)
        baseTenSum = aBaseTen + bBaseTen
        baseTenBinary = self.baseTenToBinary(baseTenSum)
        return baseTenBinary
        