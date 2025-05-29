class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sumOfNumbers = 0
        minLength=1e7
        left=0
        n = len(nums)
        for right in range(n):
            sumOfNumbers+=nums[right]
            while left<=right and sumOfNumbers>=target:
                minLength = min(minLength,right-left+1)
                sumOfNumbers-=nums[left]
                left+=1
        
        return 0 if minLength==1e7 else minLength
            
        