class Solution:
    def possible_to_divide(self,sweetness, mid, num_pieces):
        pieces_count = 0
        running_sum = 0
        
        for sweet in sweetness:
            running_sum += sweet
            if running_sum >= mid:
                pieces_count += 1
                running_sum = 0

        return pieces_count >= num_pieces


    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        n = len(sweetness)
        num_pieces = k+1
        l = 0 
        r = sum(sweetness)+1
        ans =0
    
        while l<r:
            mid = (l+r)//2
            if self.possible_to_divide(sweetness,mid,num_pieces):
                l = mid + 1
                ans = mid
            else:
                r = mid
        return ans
        