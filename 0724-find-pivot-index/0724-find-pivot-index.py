class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum,rightSum = 0,sum(nums)
        for i in range(0,n):
            leftSum +=nums[i-1] if i>0 else 0
            rightSum-=nums[i]
            if leftSum==rightSum:
                return i
        return -1
