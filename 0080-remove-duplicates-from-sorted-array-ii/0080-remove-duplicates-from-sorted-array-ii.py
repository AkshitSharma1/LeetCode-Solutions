class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p1 = 0
        m = 2
        for p2 in range(len(nums)):
            if p1-m>=0 and nums[p1-m]==nums[p2]:
                continue
            nums[p1]=nums[p2]
            p1+=1
        return p1