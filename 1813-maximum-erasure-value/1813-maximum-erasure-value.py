class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        currentSum,maxSum = 0,0
        l = 0
        n = len(nums)
        uniqueElementsSet = set()
        for r,num in enumerate(nums):
            while num in uniqueElementsSet:
                currentSum-=nums[l]
                uniqueElementsSet.remove(nums[l])
                l+=1
            currentSum+=num
            uniqueElementsSet.add(num)
            maxSum = max(maxSum,currentSum)
        return maxSum
        