class Solution:
    def isIncremental(self,nums,ii,jj):
        for i in range(1,ii):
            if nums[i]<=nums[i-1]: return False
        if ii-1>=0 and jj+1<len(nums):
            if nums[ii-1]>=nums[jj+1]: return False
        for i in range(jj+2,len(nums)):
            if nums[i]<=nums[i-1]: return False
        return True


    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        answer=0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if self.isIncremental(nums,i,j): 
                    print(i,j)
                    answer+=1
        return answer
                
        