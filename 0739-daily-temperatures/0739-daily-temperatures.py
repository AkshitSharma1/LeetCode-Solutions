class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        NBRStack = []
        for i in range(n-1,-1,-1):
            while NBRStack and nums[NBRStack[-1]]<=nums[i]:
                NBRStack.pop()
            
            ans[i] = NBRStack[-1]-i if len(NBRStack)>=1 else 0
            NBRStack.append(i)
        return ans


        