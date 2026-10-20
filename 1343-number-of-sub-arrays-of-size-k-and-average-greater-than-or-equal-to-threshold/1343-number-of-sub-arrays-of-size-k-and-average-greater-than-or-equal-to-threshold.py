class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        l = 0
        ans = 0
        n = len(arr)
        running_sum = 0
        for r in range(n):
            running_sum +=arr[r]
            while r-l+1>k:
                running_sum-=arr[l]
                l+=1
            if r-l+1==k and (running_sum/k)>=threshold: ans+=1
        return ans

                

        