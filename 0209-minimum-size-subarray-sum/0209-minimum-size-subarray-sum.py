class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        minLength = float("inf")
        l = 0
        for r in range(len(nums)):
          currentSum+=nums[r]
          while currentSum>=target:
            minLength = min(minLength,r-l+1)
            currentSum-=nums[l]
            l+=1
        
        return 0 if minLength==float('inf') else minLength
        