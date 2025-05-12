class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=j=0
        n = len(nums)
        sumOfValues=0
        answer = 1e7
        while j<n:
            sumOfValues+=nums[j]
            j+=1
            while i<j and sumOfValues>=target:
                answer = min(j-i,answer)
                sumOfValues-=nums[i]
                i+=1
        return 0 if answer==1e7 else answer


        