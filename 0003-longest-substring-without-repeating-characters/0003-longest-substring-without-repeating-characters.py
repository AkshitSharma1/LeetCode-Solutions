from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lPointer = 0
        rPointer = 0
        counter = Counter()
        length = 0
        for rPointer in range(len(s)):
            counter[s[rPointer]]+=1
            while lPointer<rPointer and counter[s[rPointer]]>1:
                counter[s[lPointer]]-=1
                lPointer+=1

            length = max(length,rPointer-lPointer+1)
        
        return length
                
            

        