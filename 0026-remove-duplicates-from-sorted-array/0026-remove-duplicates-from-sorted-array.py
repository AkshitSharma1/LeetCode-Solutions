class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftPointer = 1
        rightPointer = 1
        while rightPointer<len(nums):
            if nums[rightPointer]==nums[rightPointer-1]: 
                rightPointer+=1
            else:
                nums[leftPointer]=nums[rightPointer]
                leftPointer+=1
                rightPointer+=1
        return leftPointer

        