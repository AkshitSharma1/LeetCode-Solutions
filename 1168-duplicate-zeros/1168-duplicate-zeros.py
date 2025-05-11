class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # rightPointer will point at location where the value should come after relative shift
        rightPointer = len(arr)+arr.count(0)-1
        #leftPointer points to value that should be copied
        leftPointer = len(arr)-1
        while leftPointer>=0:
            if rightPointer<len(arr):
                arr[rightPointer]=arr[leftPointer]
            rightPointer-=1
            if arr[leftPointer]==0:
                # Duplication case
                if rightPointer<len(arr):
                    arr[rightPointer]=arr[leftPointer]
                rightPointer-=1
            leftPointer-=1



        
        """
        Do not return anything, modify arr in-place instead.
        """
     
