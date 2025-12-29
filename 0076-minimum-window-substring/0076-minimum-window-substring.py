class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frequencyMap = Counter(t)
        uniqueCharCount = len(frequencyMap)
        l = 0
        minWindow = (-1,-1)
        minWindowLength = float("inf")
        for r,char in enumerate(s):
            if char in frequencyMap:
                frequencyMap[char]-=1
                if frequencyMap[char]==0: uniqueCharCount-=1
            
            while uniqueCharCount==0:
                if minWindowLength>r-l+1:
                    minWindowLength = r-l+1
                    minWindow = (l,r)
                
                if s[l] in frequencyMap: 
                    frequencyMap[s[l]]+=1
                    if frequencyMap[s[l]]>0:
                        uniqueCharCount+=1
                l+=1
        
        return "" if minWindow[0]==-1 else s[minWindow[0]:minWindow[1]+1]
                
                
        