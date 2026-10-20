class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        curr_sum = 0
        max_sum = 0
        l = 0
        for r,num_r in enumerate(nums):
            while num_r in seen:
                seen.remove(nums[l])
                curr_sum-=nums[l]
                l+=1
            
            curr_sum += num_r
            seen.add(num_r)
            max_sum = max(max_sum,curr_sum)
        return max_sum

        