class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        n = len(matrix)
        m  = len(matrix[0])
        r = n*m -1
        while l<=r:
            mid = (l+r)//2
            row = mid//m #mid//columns
            col = mid%m #mid%columns
            if matrix[row][col]==target:
                return True
            
            if matrix[row][col]<target:
                l = mid + 1
            else:
                r = mid-1
        return False