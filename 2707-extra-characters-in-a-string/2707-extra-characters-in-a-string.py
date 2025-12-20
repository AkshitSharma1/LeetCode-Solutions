class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        keywords = set(dictionary)
        dp = [inf]*(n+1)
        dp[n] = 0
        for r in range(len(s)-1,-1,-1):
            for j in range(r,n):
                dp[r] = min(dp[r],(0 if s[r:j+1] in keywords else j-r+1) + dp[j+1])
        print(dp)
        return dp[0]


