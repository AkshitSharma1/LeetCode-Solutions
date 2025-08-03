class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=1,1
        n = len(nums)
        if n<=1: return n
        while j<n:
            if nums[j]==nums[j-1]:
                j+=1
            else:
                nums[i] = nums[j]
                j+=1
                i+=1
        return i

        