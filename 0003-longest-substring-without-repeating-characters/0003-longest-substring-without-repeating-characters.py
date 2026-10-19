class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        n = len(s)
        char_seen = set()
        for r in range(n):
            while s[r] in char_seen:
                char_seen.remove(s[l])
                l+=1
            char_seen.add(s[r])
            max_length = max(max_length,r-l+1)
        return max_length
