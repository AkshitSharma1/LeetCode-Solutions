class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        
        def countLessThan(num):
            #find coutn of numbers <= num
            #staicase method
            r = n-1
            c = 0
            count = 0

            while r>=0 and c<n:
                if matrix[r][c]<=num:
                    #all numbers in this col above it <=num
                    count += r+1
                    c+=1
                else:
                    #matrix[r][c]>num
                    r-=1
            return count
        
        l = -(10**9+1)
        r = +(10**9+1)
        ans = float("inf")
        while l<=r:
            mid = (l+r)//2
            if countLessThan(mid)>=k:
                #this can eb a possible answer
                #we store this
                ans = min(ans,mid)
                #search for more possible answers
                r = mid-1
            else:
                #ans must be to the right
                l = mid+1
        return int(ans)

