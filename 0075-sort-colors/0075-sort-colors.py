class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pi = 0 #write pointer
        for pj in range(len(nums)):
            if nums[pj]==0:
                nums[pi],nums[pj] = nums[pj],nums[pi]
                pi+=1
        
        for pj in range(pi,len(nums)):
            if nums[pj]==1:
                nums[pi],nums[pj] = nums[pj],nums[pi]
                pi+=1
    
        
        