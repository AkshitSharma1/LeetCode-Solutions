class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        i = 0
        while j<len(nums):
            if nums[j]==val:
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
        return i 
        