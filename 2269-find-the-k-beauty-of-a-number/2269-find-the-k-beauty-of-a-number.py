class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        l = 0
        num_str = str(num)
        curr_num = 0
        for r in range(len(num_str)):
            curr_num = curr_num*10 + int(num_str[r])
            while r-l+1>k:
                #remove the leftmost value from this number
                curr_num %= 10**(r-l)
                l+=1
            
            if r-l+1==k and curr_num!=0 and num%curr_num==0: ans+=1
        return ans

