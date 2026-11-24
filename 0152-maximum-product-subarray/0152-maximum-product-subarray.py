class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        @cache
        def f(i,flag):
            #flag = 1-> means we want the max product of subarray that ends at position i, else we want min product
            answer = 0
            if i<0:
                return 1
            if flag==1:
                answer = max(f(i-1,1)*nums[i],f(i-1,0)*nums[i],nums[i])
            else:
                answer = min(f(i-1,1)*nums[i],f(i-1,0)*nums[i],nums[i])
            return answer
 
        max_value = max(max([f(i,0) for i in range(n)]),max([f(i,1) for i in range(n)]))
        return max_value

