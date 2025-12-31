class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0: return 0
        l = 0
        r = x+1
        ans = -1
        while l<r:
            m = (l+r)//2
            if m*m<x:
                l = m+1
                ans = m
            elif m*m==x: return m
            else:
                r = m
        return ans

        