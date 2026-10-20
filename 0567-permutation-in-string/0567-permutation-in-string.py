class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        char_count = Counter(s1)
        char_count_copy = char_count.copy()
        zero_freq_char_count = 0
        l = 0
        s  = s2
        for r in range(n):
            if s[r] not in char_count_copy:
                l = r + 1
                char_count_copy = char_count.copy()
                zero_freq_char_count = 0
                continue
            

            char_count_copy[s[r]]-=1
            if char_count_copy[s[r]]==0: zero_freq_char_count+=1

            while r-l+1>m:
                char_count_copy[s[l]]+=1
                if char_count_copy[s[l]]==1: zero_freq_char_count-=1
                l+=1
            
            if r-l+1==m and zero_freq_char_count==len(char_count): return True
        return False




        