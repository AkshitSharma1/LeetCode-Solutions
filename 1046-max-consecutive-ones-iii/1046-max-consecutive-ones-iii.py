class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,flipCount = 0,0
        answer = 0
        for r,num in enumerate(nums):
            if num==0:
                flipCount+=1
            while flipCount>k:
                if nums[l]==0:
                    flipCount-=1
                l+=1
            answer = max(answer,r-l+1)
        return answer

        