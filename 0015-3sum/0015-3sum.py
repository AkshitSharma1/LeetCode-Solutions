class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        num.sort(key=lambda x:x)
        n = len(num)
        answer = []
        for start in range(n):
            if start>0 and num[start]==num[start-1]: continue
            i = start+1
            j = n-1
            while i<j and i<n and j>0:
                sumOfValues = num[i]+num[j]+num[start]
                if sumOfValues>0: 
                    j-=1
                elif sumOfValues<0:
                    i+=1
                elif sumOfValues==0:
                    answer.append([num[start],num[i],num[j]])
                    i+=1
                    while i<n and num[i]==num[i-1]: i+=1
        return answer
        