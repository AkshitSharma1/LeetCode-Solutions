class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #dp(i)-> min number of chars left when s[0:i] is broken optimally
        #dp(i) = min( dp(i), for j in range(i) dp(j) + 0 if s[j:i] in dictionary else i-j
        # dp(0) = 0
        # dp(1) = 0 if s[0] in dictionary else 1
        dictionary = set(dictionary) 
        @cache
        def dp(i):
            nonlocal dictionary
            if i==0: return 0
            answer = float("inf")
            for j in range(i):
                answer = min(answer,dp(j)+(0 if s[j:i] in dictionary else i-j))
            return answer
        return dp(len(s))