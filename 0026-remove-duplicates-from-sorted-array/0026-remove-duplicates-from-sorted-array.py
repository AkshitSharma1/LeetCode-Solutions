class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1
        while j<len(nums):
            if nums[j]==nums[j-1]: 
                j+=1
                continue
            nums[i] = nums[j]
            i+=1
            j+=1
        return i


        