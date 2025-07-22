class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        def helperFunction(index):
            #Whats the length of longest increasing subsequence starting at index i?
            if index>=n: return 0
            if dp[index]!=-1: return dp[index]
            maxLengthStartingAtI = 1
            for j in range(index+1,n):
                if nums[j]>nums[index]:
                    maxLengthStartingAtI = max(maxLengthStartingAtI,
                    helperFunction(j)+1)
            dp[index] = maxLengthStartingAtI
            return dp[index]
        
        for i in range(len(nums)): helperFunction(i)
        return max(dp)
        

        