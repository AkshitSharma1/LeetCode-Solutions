class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        i = 0
        j = 0
        for j in range(len(s)):
            was_duplicate = i>0 and s[j] ==s[i-1]
            while i>0 and s[j]==s[i-1]:
                i-=1
            if was_duplicate==False:
                s[i] = s[j]
                i+=1
        return "".join(s[:i])
            