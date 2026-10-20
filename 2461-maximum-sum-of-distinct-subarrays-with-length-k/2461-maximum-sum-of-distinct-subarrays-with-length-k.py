class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        r = 0
        l = 0
        max_subarray_sum = 0
        curr_subarray_sum = 0
        seen = set()
        for r,num in enumerate(nums):
            while nums[r] in seen:
                seen.remove(nums[l])
                curr_subarray_sum-=nums[l]
                l+=1
            
            #now we process nums[r]
            curr_subarray_sum+=nums[r]
            seen.add(nums[r])
            while r-l+1>k:
                seen.remove(nums[l])
                curr_subarray_sum-=nums[l]
                l+=1
            
            if r-l+1==k:
                max_subarray_sum = max(max_subarray_sum,curr_subarray_sum)
        return max_subarray_sum
                
            

        