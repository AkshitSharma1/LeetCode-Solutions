class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left,right=0,0
        n = len(nums)
        while right<n:
            while right<n and nums[right]==0:
                right+=1
            if right==n: break

            nums[left]=nums[right]
            left+=1
            right+=1

        while left<n: 
            nums[left]=0
            left+=1
        return nums
        