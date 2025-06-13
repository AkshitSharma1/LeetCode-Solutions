class Solution:
    def tribonacci(self, n: int) -> int:

        def sol(n):
            if n<=0: return 0
            if n==1: return 1
            if n==2: return 1
            if dp[n]!=-1: return dp[n]
            dp[n] = sol(n-1)+sol(n-2)+sol(n-3)
            return dp[n]

        dp = [-1]*(n+1)
        return sol(n)    
    
        