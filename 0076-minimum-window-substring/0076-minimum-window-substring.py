class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #let length s = n, len t = m
        l = 0
        char_goal = Counter(t)
        min_length = float("inf")
        ans = None
        zero_freq_char_count = 0
        n = len(s)
        for r in range(n):
            if s[r] in char_goal:
                char_goal[s[r]]-=1
                if char_goal[s[r]]==0: zero_freq_char_count+=1

            while zero_freq_char_count==len(char_goal):
                if (r-l+1<min_length):
                    min_length = r-l+1
                    ans = [l,r]
                if s[l] in char_goal:
                    char_goal[s[l]]+=1
                    if char_goal[s[l]]==1: zero_freq_char_count-=1
                l+=1
        
        if ans is None:
            return ""
        l,r = ans
        return s[l:r+1]



