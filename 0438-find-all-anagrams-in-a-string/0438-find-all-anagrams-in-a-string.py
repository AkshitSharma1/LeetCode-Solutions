from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_char_count = Counter(p)
        zero_value_count = 0
        l = 0
        m = len(p)
        n = len(s)
        ans = []

        for r in range(n):
            if s[r] not in p_char_count:
                p_char_count = Counter(p)
                zero_value_count = 0
                l = r+1
                continue

            p_char_count[s[r]]-=1
            if p_char_count[s[r]]==0: zero_value_count+=1

            while p_char_count[s[r]]<0:
                p_char_count[s[l]]+=1
                if p_char_count[s[l]]==1: zero_value_count-=1
                l+=1

            if zero_value_count==len(p_char_count):
                ans.append(l)

        return ans