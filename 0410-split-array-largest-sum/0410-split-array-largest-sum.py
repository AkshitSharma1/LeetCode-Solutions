class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        #dp(i,k) = minimized largest sum of any  subarray when [0:i+1] indexes are split into k group
        # we want dp(len(nums)-1,k)
        #dp(i,k) =  j such that max(dp(j,k-1),sum(arr[j+1:i+1]) is minimized 
        @cache
        def dp(i,k):
            nonlocal nums
            answer = float('inf')
            #base case-> k=1 , j=0:
            if k==1:
                return sum(nums[0:i+1])
            
            subarray_sum =sum( nums[0:i+1])
            for j in range(i):
                subarray_sum-=nums[j]
                answer = min(answer,max(dp(j,k-1),subarray_sum))
            return answer
        return dp(len(nums)-1,k)


        