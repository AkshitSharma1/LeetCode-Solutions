class Solution:
    def nextGreaterElement(self, n: int) -> int:
        number = list(str(n))
        flag = False
        for i in range(len(number)-2,-1,-1):
            if number[i]<number[i+1]: 
                flag = True
                break
        if flag==False:
            return -1
        
        for j in range(len(number)-1,-1,-1):
            if number[j]>number[i]:
                number[j],number[i] = number[i],number[j]
                break
        number[i+1:] = sorted(number[i+1:])
        return int(''.join(number)) if int(''.join(number)) <=2**31 - 1 else -1

        