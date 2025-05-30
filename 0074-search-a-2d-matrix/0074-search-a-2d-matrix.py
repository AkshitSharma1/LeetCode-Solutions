class Solution:
    def binarySearchAlongRow(self,matrix,colNumber,target):
        low = 0
        high = len(matrix)-1
        while low<=high:
            mid = (low+high)//2
            if matrix[mid][colNumber]==target:
                return mid
            elif matrix[mid][colNumber]<target:
                low = mid+1
            else:
                high = mid - 1
        
        
        return high
    
    def binarySearchAlongColumn(self,matrix,rowNumber,target):
        low = 0
        high = len(matrix[0])-1
        while low<=high:
            mid = (low+high)//2
            if matrix[rowNumber][mid]==target:
                return True
            elif matrix[rowNumber][mid]<target:
                low = mid+1
            else :
                high = mid-1
            
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binarySearchAlongColumn(
            matrix,self.binarySearchAlongRow(
                matrix,0,target
            ),target
        )

        