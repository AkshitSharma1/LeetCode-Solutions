class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)#rows
        n = len(mat[0])
        #approach- apply binary search across rowss
        l = 0
        r = m-1
        while l<=r:
            #find mid row
            mid = (l+r)//2
            #find max col index
            max_col_index = max(range(n), key=lambda i: mat[mid][i])
            #this will be max in current row-> compare up and down
            if (mid==0 or mat[mid][max_col_index]>mat[mid-1][max_col_index]) and (mid==m-1 or mat[mid][max_col_index]>mat[mid+1][max_col_index]):
                return [mid,max_col_index]
            
            if mid<m-1 and mat[mid][max_col_index]<mat[mid+1][max_col_index]:
                l=mid+1
            else:
                r = mid-1
        return -1

        