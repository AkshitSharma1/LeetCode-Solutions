class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        last_num =0
        for num in arr:
            diff = num - last_num-1
            if diff==0:
                last_num = num
                continue
            else:
                #c1 the diff is less than k
                # in this case the number does not lie over here in this gap
                if diff<k:
                    last_num = num
                    k-= diff
                    continue
                else:
                    #number lies over here
                    return last_num + k
        return arr[-1]+k
            
