class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = 0
        r = 10**14
        def getMagicalCount(n):
            return n//a + n//b - (n//lcm(a,b))
        ans = float("inf")
        while l<=r:
            m = (l+r)//2
        
            magical_count = getMagicalCount(m)
            if magical_count>=n:
                r = m-1
                ans = min(ans,m)
            else:
                l = m+1
        return int(ans % (1e9+7))