class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) #number of rows
        m = len(matrix[0]) #number of columns

        r = 0
        c = m-1
        while r<n and c>=0 :
            if matrix[r][c]==target: return True
            if matrix[r][c]<target:
                #target must be down-> so increase the row number
                r+=1
            else:
                #case when matrix[r][c]>target:
                #target must be to the left-> decrease column number
                c-=1
        return False