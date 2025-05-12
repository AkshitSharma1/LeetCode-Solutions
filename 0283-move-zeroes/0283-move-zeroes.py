class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        leftPointer = 0
        rightPointer = 0
        n = len(arr)
        while rightPointer<n:
            if arr[rightPointer]==0: 
                rightPointer+=1
            else:
                arr[leftPointer]=arr[rightPointer]
                leftPointer+=1
                rightPointer+=1
            
        while leftPointer<n:
            arr[leftPointer]=0
            leftPointer+=1
        

