class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pi = 0
        pj = 0
        n = len(nums)
        while pj<n:
            if nums[pj]!=val:
                nums[pi] = nums[pj]
                pi+=1
            pj+=1
        return pi