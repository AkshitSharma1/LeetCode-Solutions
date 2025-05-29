class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        #O(26*N)
        # Fix the number of unique characters 
        maxLength = 0
        for fixedUniqueCharCount in range(1,27):
            numUniqueCharCount = 0
            frequencyGreaterThanK=0
            counter = Counter()
            left=0
            for right in range(len(s)):
                counter[s[right]]+=1
                if counter[s[right]]==1: numUniqueCharCount+=1
                if counter[s[right]]==k: frequencyGreaterThanK+=1

                while left<=right and numUniqueCharCount>fixedUniqueCharCount:
                    counter[s[left]]-=1
                    if counter[s[left]]==0: numUniqueCharCount-=1
                    if counter[s[left]]==k-1: frequencyGreaterThanK-=1
                    left+=1
                
                if numUniqueCharCount==fixedUniqueCharCount and frequencyGreaterThanK==fixedUniqueCharCount:
                    maxLength = max(maxLength,right-left+1)
                
        
        return maxLength

        