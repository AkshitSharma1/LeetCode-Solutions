class Solution:
    def getCommon(self, num1: List[int], num2: List[int]) -> int:
        num1Pointer=0
        num2Pointer=0
        while num1Pointer<len(num1) and num2Pointer<len(num2):
            numb1Value = num1[num1Pointer]
            numb2Value = num2[num2Pointer]
            if numb1Value==numb2Value: return numb1Value
            elif numb1Value>numb2Value: num2Pointer+=1
            elif numb1Value<numb2Value: num1Pointer+=1
        
        return -1

        