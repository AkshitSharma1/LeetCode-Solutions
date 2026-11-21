class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        #dp{i}- largest sum after partioning arr from indices 0 to i-1 both inclusive
        #we want dp(len(arr))
        #dp(i) = for j in range(0,i) dp(j) +  max(arr[j:i])*(i-j)
        #basecase-> dp(0) = 0, dp(1) = arr[0]
        @cache
        def dp(i):
            nonlocal arr
            if i==0: return 0
            if i==1: return arr[0]
            answer = float("-inf")
            for j in range(max(0,i-k),i):
                answer = max(answer,dp(j)+max(arr[j:i])*(i-j))
            return answer
        return dp(len(arr))