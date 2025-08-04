class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        if target<0: return -1
        currentSum = 0
        n = len(nums)
        l=0
        slidingWindowSize = -float('inf')
        #We will want maximum sliding window size
        for r in range(n):
            currentSum+=nums[r]
            while currentSum>target:
                currentSum-=nums[l]
                l+=1
            if currentSum==target:
                slidingWindowSize = max(slidingWindowSize,r-l+1)
        
        return -1 if slidingWindowSize==-float('inf') else n-slidingWindowSize

        