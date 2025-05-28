from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        left,right = 0,0
        counter = Counter()
        uniqueCharCount = 0
        for char in t:
            counter[char]+=1
            if counter[char]==1:
                uniqueCharCount+=1
        

        length = 1e7
        ans=""
        left=0
        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]]-=1
                if counter[s[right]]==0: uniqueCharCount-=1
          
            while uniqueCharCount==0 and left<=right:

                
                if right-left+1<length:
                    length = right-left+1
                    ans = s[left:right+1]

                if s[left] in counter:
                    counter[s[left]]+=1
                    if counter[s[left]]==1: uniqueCharCount+=1
                left+=1
        return ans
            

