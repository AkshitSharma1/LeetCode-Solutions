class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right=1,1
        n = len(nums)
        while right<n:
            while right<n and nums[right]==nums[right-1]:
                right+=1
            
            if right==n: break

            nums[left] = nums[right]
            left+=1
            right+=1

        return left

        