from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter()
        distinctCharCount=0
        if len(p)>len(s): return []
        for char in p:
            counter[char]+=1
            if counter[char]==1: distinctCharCount+=1
        
        
        #First, grow the window to required length
        i=j=0

        for j in range(len(p)):
            if s[j] in counter:
                counter[s[j]]-=1
                if counter[s[j]]==0: distinctCharCount-=1
        answer = []
        while j<len(s):
            #Compare the values
            if distinctCharCount==0:
                answer.append(i)
            
            if s[i] in counter:
                counter[s[i]]+=1
                if counter[s[i]]==1: distinctCharCount+=1
            i+=1

            j+=1

            if j<len(s) and s[j] in counter:
                counter[s[j]]-=1
                if counter[s[j]]==0: distinctCharCount-=1
        
        return answer


        
        