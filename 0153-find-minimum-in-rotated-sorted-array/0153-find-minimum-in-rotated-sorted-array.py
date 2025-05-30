class Solution:
    def findMin(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        ans=0

        while low<=high:
            mid = (low+high)//2
            if arr[mid]<=arr[high]:
                high = mid
                ans = arr[mid]
                #possible ans, save it
            else:
                low = mid+1
            
            if low==high: return arr[high]
        return ans
        