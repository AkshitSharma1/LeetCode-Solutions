class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i,j = 0,0
        nums.sort()
        n = len(nums)
        current_sum = 0
        answer = []
        for k  in range(n):
            if k>0 and nums[k]==nums[k-1]: continue
            i = k+1
            j = len(nums)-1
            while i<j and i<n and j<n:
                current_sum = nums[i]+nums[j]+nums[k]
                if current_sum<0:
                    i+=1
                elif current_sum>0:
                    j-=1
                else:
                    answer.append([nums[k],nums[i],nums[j]])
                    i+=1
                    while i>k+1 and i<n and nums[i]==nums[i-1]: i+=1
                #while j>=0 and j<n-1 and nums[j]==nums[j+1]: j-=1
        return answer

                
