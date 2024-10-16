class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumOfSubArray = -1e7
        tempSumOfSubArray = 0
        lPointer=0
        rPointer=0
        while (rPointer<len(nums)):
            tempSumOfSubArray +=nums[rPointer]
            sumOfSubArray = max(tempSumOfSubArray,sumOfSubArray)
            if tempSumOfSubArray<0:
                lPointer=rPointer+1
                tempSumOfSubArray=0
            rPointer+=1
        return sumOfSubArray

        