class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        uniqueChars = set()
        maxLength = 0
        for r in range(len(s)):
            if s[r]  in uniqueChars:
                while s[r] in uniqueChars:
                    uniqueChars.remove(s[l])
                    l+=1
                
            uniqueChars.add(s[r])
            maxLength = max(maxLength,r-l+1)
        return maxLength



        