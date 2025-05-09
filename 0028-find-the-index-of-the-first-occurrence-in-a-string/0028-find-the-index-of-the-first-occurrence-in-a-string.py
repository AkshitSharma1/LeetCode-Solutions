from collections import deque
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i = 0
        j = 0
        while j<len(needle) and i<len(haystack):
            if needle[j]==haystack[i]:
                i+=1
                j+=1
            else:
                
                i=i-j+1
                j=0
            
        
        if len(needle)==j: return i-j
        return -1

        