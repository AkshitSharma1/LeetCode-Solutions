class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        seen_char = set()
        n = len(s)
        l = 0
        ans = 0
        for r in range(n):
            while s[r] in seen_char:
                seen_char.remove(s[l])
                l+=1
            seen_char.add(s[r])
            while r-l+1>3:
                seen_char.remove(s[l])
                l+=1
            if r-l+1==3: ans+=1
        return ans