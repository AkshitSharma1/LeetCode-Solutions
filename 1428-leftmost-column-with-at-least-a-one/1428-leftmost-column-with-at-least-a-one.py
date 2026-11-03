# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n,m = binaryMatrix.dimensions()
        l = 0
        r =m-1 #number of cols
        min_one_index = float("inf") 
        for row in range(n):
            #find leftmost for this row
            l = 0
            r = m-1
            while l<=r:
                mid = (l+r)//2
                if binaryMatrix.get(row,mid)<1:
                    l=mid+1
                else:
                    min_one_index = min(min_one_index,mid)
                    r = mid-1
        return min_one_index if min_one_index<10**7 else -1
