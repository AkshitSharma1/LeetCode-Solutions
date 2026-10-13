class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pi = 0
        n = len(nums)
        for pj in range(0,n-1):
            if nums[pj]==nums[pj+1]: continue
            nums[pi] = nums[pj]
            pi+=1
        
        nums[pi] = nums[n-1]
        pi+=1
        return pi
