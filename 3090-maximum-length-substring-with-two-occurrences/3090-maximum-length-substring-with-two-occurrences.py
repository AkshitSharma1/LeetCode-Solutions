class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_count = {c:2 for c in set(s)}
        l = 0
        max_len = 0 
        n = len(s)
        for r in range(n):
            char_count[s[r]]-=1
            while char_count[s[r]]<0:
                char_count[s[l]]+=1
                l+=1
            max_len = max(max_len,r-l+1)
        return max_len