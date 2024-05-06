# https://leetcode.com/problems/apply-discount-to-prices/description/
# This one was actually pretty tough
class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        discountPercent = (100.0 - discount) / 100.0
        priceMap = {}
        words = sentence.split()

        for i in range(len(words)):
            word = words[i]
            price = ""
            isPrice = True
            for j in range(len(word)):
                letter = word[j]
                if j == 0 and letter != "$":
                    isPrice = False
                    break
                elif j > 0 and letter.isdigit() == False:
                    isPrice = False
                    break
            if isPrice:
                price = word[1:]

            if len(price) > 0:
                discountedPrice = "$" + str(round(int(price) * discountPercent, 2))
                if len(discountedPrice.split('.')[1]) < 2:
                    # add trailing zero
                    discountedPrice += "0"

                priceMap[i] = ("$" + price, discountedPrice)
                words[i] = discountedPrice
        
        sentence = " ".join(words)
        return sentence