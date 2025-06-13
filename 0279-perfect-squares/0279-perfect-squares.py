class Solution:
    def numSquares(self, n: int) -> int:
        def sol(n):
            if n<=0: return 0
            if n==1: return 1
            if dp[n]!=-1: return dp[n]
            sqrt = int(n**(1/2))
            count = float("inf")
            for i in range(1,sqrt+1):
                count = min(count,1+sol(n-i**2)) 
            dp[n] = count
            return dp[n]
        dp = [-1]*(n+1)
        return sol(n)

        