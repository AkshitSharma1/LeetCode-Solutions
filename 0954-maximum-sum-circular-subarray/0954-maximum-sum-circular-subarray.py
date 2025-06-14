class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l=0
        r=0
        n = len(nums)
        currSum=0
        maxSum = float("-inf")
        while r<n:
            currSum+=nums[r]
            maxSum = max(currSum,maxSum)

            if currSum<0:
                l=r+1
                currSum = 0
            r+=1
        
        #C2 - Circular, find minimum sum
        maxSumCircular =float("inf")
        currSumCircular=0
        r = 0
        while r<n:
            currSumCircular+=nums[r]
            maxSumCircular = min(maxSumCircular,currSumCircular)
        
            if currSumCircular>0:
                currSumCircular=0
            r+=1
        print(sum(nums),maxSumCircular,maxSum)
        if sum(nums)-maxSumCircular==0: return maxSum
        return max(sum(nums)-1*maxSumCircular,maxSum)


        