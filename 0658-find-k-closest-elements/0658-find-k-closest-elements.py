class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = n-1
        while r-l+1>k:
            if abs(arr[r]-x)<abs(arr[l]-x):
                l+=1
            else:
                r-=1
        return arr[l:r+1]


        