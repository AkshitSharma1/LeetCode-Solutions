class Solution:
    def minCut(self, s: str) -> int:
        #base case-> char of length 1-> always pallindrome
        #dp[i]-> number of minimum cuts to partition {0....i-1 both inclusive}
        #base case-> dp[1] = 1, 
        #dp[i] = 1+  min(dp[i-length] if current s[i-length:i] is pallindrome
        # we want dp length n
        def isPallindrome(s): return s==s[::-1]
        @cache
        def f(i):
            if i==1: return 0
            if i==0: return 0
            answer = float("inf")
            for length in range(1,i+1):
                if isPallindrome(s[i-length:i]):
                    if i==length: return 0
                    answer = min(answer,1 + f(i-length))
            return answer

        return f(len(s))

