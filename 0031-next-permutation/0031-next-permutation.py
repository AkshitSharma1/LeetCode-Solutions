class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Find first element such that a[i]<a[i+1]
        i = len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i<0: return nums.reverse()                                                                                                                                                                                      
        #Now find j, where j>i and nums[j] >nums[i] (rightmost 1st element)
        j = len(nums)-1
        while j>i and nums[j]<=nums[i]:
            j-=1
        
        nums[i],nums[j] = nums[j],nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        return nums
        