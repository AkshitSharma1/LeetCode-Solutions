class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = [-1,-1]
        min_length = float("inf")
        l = 0
        char_count = Counter(t)
        non_zero_char_count = len(char_count)
        n = len(s)
        for r in range(n):
            #Grow the window
            if s[r] in char_count: 
                char_count[s[r]]-=1
                if char_count[s[r]]==0: non_zero_char_count-=1
            
            while non_zero_char_count==0:
                #we have covered all chars of t
                #valid ans store this
                if (r-l+1)<min_length:
                    min_length = r-l+1
                    ans = [l,r]
                if s[l] in char_count:
                    char_count[s[l]]+=1
                    if char_count[s[l]]==1: 
                        non_zero_char_count+=1
                        l+=1
                        break
                l+=1
        l,r = ans
        return s[l:r+1]
            
