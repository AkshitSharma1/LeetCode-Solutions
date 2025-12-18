class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = defaultdict(int)
        dp[n] = 1
   
        for j in range(n-1,-1,-1):
            if s[j]=='0':
                dp[j] = 0
            else:
                dp[j] = dp[j+1]
                if j<=n-2 and (int(s[j])*10+int(s[j+1]))<=26:
                    dp[j]+=dp[j+2]
        return dp[0]
