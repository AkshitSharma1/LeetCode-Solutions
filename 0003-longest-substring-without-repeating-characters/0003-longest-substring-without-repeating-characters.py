from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Grow window
        i = 0
        n = len(s)
        j = 0
        ans=0
        counter = Counter()
        while j<n:
            counter[s[j]]+=1
            j+=1
            
            while counter[s[j-1]]>1:
                counter[s[i]]-=1
                i+=1
            ans = max(ans,j-i)
        return ans


        