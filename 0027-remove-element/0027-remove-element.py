class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j=0,0
        n = len(nums)
        while j<n:
    
            if nums[j]==val:
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
        return i