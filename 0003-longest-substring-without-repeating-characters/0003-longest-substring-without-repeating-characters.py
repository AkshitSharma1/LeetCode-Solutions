class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        answer = 0
        l = 0
        n = len(s)
        for r in range(n):
            while s[r] in char_set and l<r:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            answer = max(answer,r-l+1)
        return answer
            


        