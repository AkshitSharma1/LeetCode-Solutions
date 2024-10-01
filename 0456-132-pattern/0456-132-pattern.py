class Solution:
    def find132pattern(self, nums):
        n = len(nums)
        st = []
        NGLIndex = [-1]*n
        minElement = [nums[0]]*n
        
        for i in range(n):
            minElement[i] = min(minElement[i-1],nums[i])
            while st and st[-1][0]<nums[i]:
                st.pop()
            if st:
                NGLIndex[i] = st[-1][1]
            st.append((nums[i],i))
        for i in range(n-1,-1,-1):
            if NGLIndex[i]!=-1 and NGLIndex[i]!=0:
                if minElement[NGLIndex[i]-1]<nums[i] and nums[NGLIndex[i]]>nums[i]:
                    return True
        return False

