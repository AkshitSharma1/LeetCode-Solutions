class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pi = 1
        n = len(nums)
        for pj in range(1,n):
            if nums[pj]==nums[pj-1]: continue
            nums[pi] = nums[pj]
            pi+=1
        return pi
