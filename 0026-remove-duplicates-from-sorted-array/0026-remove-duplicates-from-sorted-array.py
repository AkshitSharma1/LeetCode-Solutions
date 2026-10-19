class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)<=1: return len(nums)
        pi = 1
        pj = 1
        n = len(nums)
        while pj<n:
            if nums[pj]!=nums[pj-1]:
                nums[pi] = nums[pj]
                pi+=1
            pj+=1
        return pi


        