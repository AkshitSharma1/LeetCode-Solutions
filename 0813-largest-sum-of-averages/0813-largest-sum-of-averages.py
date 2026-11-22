class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        #dp[i][k] # number of ways to divide numbers 0,1,2...i both inclusive into upto k groupssuch that the sum is maximum of avgs
        # recursive-> dp[i][k] = for j in range(0,i) dp(j,k-1) + avg(nums[j+1:i+1])
        #basecase-> k=1 , dp[i][k] = avg(nums[0:i+1])
        def avg(arr): return sum(arr)/len(arr)

        @cache
        def dp(i,k):
            #Basecase
            if k==1: return avg(nums[0:i+1])
            answer = float("-inf")
            running_sum = sum(nums[0:i+1])
        
            for j in range(i):
                running_sum-=nums[j]
                new_avg = (running_sum)/(i-j)
                answer = max(answer,dp(j,k-1)+new_avg)
            return answer
        return dp(len(nums)-1,k)
            
