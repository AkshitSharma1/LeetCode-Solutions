class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # rightPointer will point at location where the value should come after relative shift
        n = len(arr)
        rightPointer = n+arr.count(0)-1

        #leftPointer points to value that should be copied
        leftPointer = n-1
        while leftPointer>=0:
            if rightPointer<n:
                arr[rightPointer]=arr[leftPointer]
            rightPointer-=1
            if arr[leftPointer]==0:
                # Duplication case
                if rightPointer<n:
                    arr[rightPointer]=arr[leftPointer]
                rightPointer-=1
            leftPointer-=1



        
        """
        Do not return anything, modify arr in-place instead.
        """
     
