class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        for j in range(n):
            while i<j and nums[i]==0: i+=1
            if nums[j]==0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        
        i=0
        j = 0
        for j in range(n):
            while i<j and (nums[i]==0 or nums[i]==1): i+=1
            if nums[j] ==1:
                nums[i],nums[j] = nums[j],nums[i]
        return nums

        