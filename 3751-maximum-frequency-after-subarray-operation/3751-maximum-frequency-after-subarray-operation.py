class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        totalKCount = nums.count(k)
        maxKViaSubWindow = 0
        for numberToSwap in range(1,51):
            maxSumSoFar = 0
            currentMaxSum = 0
            for r,num in enumerate(nums):
                variation = 0
                if num==numberToSwap: variation=1
                if num==k: variation=-1
                currentMaxSum = max(0,currentMaxSum+variation )
                maxSumSoFar = max(currentMaxSum,maxSumSoFar)
            maxKViaSubWindow = max(maxKViaSubWindow,maxSumSoFar)
        return maxKViaSubWindow + totalKCount
        