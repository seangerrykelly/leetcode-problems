class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currIndex = len(arr) - 1
        greatestElement = arr[currIndex]
        arr[currIndex] = -1
        currIndex -= 1
        while currIndex >= 0:
            currElement = arr[currIndex]
            arr[currIndex] = greatestElement
            
            if currElement > greatestElement:
                greatestElement = currElement
            currIndex -= 1
        
        return arr