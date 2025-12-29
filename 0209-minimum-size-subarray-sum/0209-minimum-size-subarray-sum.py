class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = float("inf")
        running_sum = 0
        l = 0
        for r in range(len(nums)):
            running_sum+=nums[r]
            while running_sum>=target:
                answer = min(answer,r-l+1)
                running_sum-=nums[l]
                l+=1
        return 0 if answer>=float('inf') else answer
