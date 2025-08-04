class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMostKSum(k):
            currentSum = 0
            answer = 0
            l = 0
            for r,num in enumerate(nums):
                currentSum+=num
                while l<=r and currentSum>k:
                    currentSum-=nums[l]
                    l+=1
                if currentSum<=k:
                    answer +=(r-l+1)
            return answer
        
        return atMostKSum(goal)-atMostKSum(goal-1)
        