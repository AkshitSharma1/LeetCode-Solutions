class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l=0
        r = len(s)-1
        while(l<=r):
            if ((s[l].isalpha() or s[l].isnumeric())==False):
                l+=1
                continue
            
            if ((s[r].isalpha() or s[r].isnumeric())==False):
                r-=1
                continue
            
            if (s[l]!=s[r]): return False
            l+=1
            r-=1
        return True
            
            
        