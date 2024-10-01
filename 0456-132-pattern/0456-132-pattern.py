class Solution:
    def find132pattern(self, nums):
        n = len(nums)
        minElementToLeft = [0] * n
        minElementToLeft[0] = nums[0]
        
        for i in range(1, n):
            minElementToLeft[i] = min(nums[i], minElementToLeft[i - 1])
        
        # Stack to find NEXT GREATER ELEMENT TO LEFT
        st = []
        NGLIndex = [-1] * n
        
        for i in range(n):
            while st and st[-1][0] <= nums[i]:
                st.pop()
            if st:
                NGLIndex[i] = st[-1][1]
            st.append((nums[i], i))
        
        for k in range(n - 1, 0, -1):
            j = NGLIndex[k]
            if j == 0 or j == -1:
                continue
            if minElementToLeft[j - 1] < nums[k]:
                return True
        
        return False
