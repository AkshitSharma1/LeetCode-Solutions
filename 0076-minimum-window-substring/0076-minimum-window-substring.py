from collections import Counter
from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter()
        nonZeroCount =0
        for char in t:
            counter[char]+=1
            if counter[char]==1: nonZeroCount+=1
        
        #Grow the window
        minWindowI = 0
        minWindowJ = 0
        minWindowLength = math.inf
        i=0
        j=0
        n = len(s)

        while j<n:
            if s[j] in counter:
                counter[s[j]]-=1
                if counter[s[j]]==0: nonZeroCount-=1
            
                #Check if nonZeroCount is 0
                while i<=j and nonZeroCount==0:
                    #Try to shrink window
                    if j-i+1<minWindowLength:
                        minWindowLength = j-i+1
                        minWindowI = i
                        minWindowJ = j+1

                    if s[i] in counter:
                        counter[s[i]]+=1
                        if counter[s[i]]==1: nonZeroCount+=1
                    i+=1
            j+=1
        return s[minWindowI:minWindowJ]

                    




        