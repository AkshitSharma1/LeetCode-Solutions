class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        maxSum = 0
        l = 0
        elements = set()
        n = len(nums)
        for r,num in enumerate(nums):
            while num in elements:
                currentSum-=nums[l]
                elements.remove(nums[l])
                l+=1
            

            currentSum+=num
            elements.add(num)

            while r-l+1>k:
                currentSum-=nums[l]
                elements.remove(nums[l])
                l+=1
            
            if r-l+1==k: maxSum = max(maxSum,currentSum)
        return maxSum