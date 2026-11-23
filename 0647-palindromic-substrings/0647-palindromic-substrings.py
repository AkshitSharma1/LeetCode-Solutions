class Solution:
    def countSubstrings(self, s: str) -> str:
        n = len(s)
        answer = 0
        for i in range(len(s)):
            max_length = 0
            #count even 
            l = i-1
            r = i
            while l>=0 and r<n and s[l]==s[r]:
                max_length+=1
                l-=1
                r+=1
            
            #now we count odd length pallindromes
            l = i
            r = i
            while l>=0 and r<n and s[l]==s[r]:
                max_length +=1
                l-=1
                r+=1
            answer +=max_length
        return answer
