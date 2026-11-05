class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l = 0
        r = 10**11
        k = n

        def uglyPosition(num):
            return num//a + num//b + num//c-num//lcm(a,b) -num//lcm(b,c) -num//lcm(a,c) + num//lcm(a,lcm(b,c))
        ans = 0
        while l<=r:
            m = (l+r)//2
            ugly_position = uglyPosition(m)

            if ugly_position>=k:
                ans = m
                r = m-1
            else:
                l= m+1
        return ans