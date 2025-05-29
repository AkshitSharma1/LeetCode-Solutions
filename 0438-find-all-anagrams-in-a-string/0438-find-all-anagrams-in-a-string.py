from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        n = len(s)
        ans = []
        left=0
        numDifferentChar=len(counter)
        print(numDifferentChar,counter)
        for right in range(n):
            if s[right] in counter:
                counter[s[right]]-=1
                if counter[s[right]]==0:
                    numDifferentChar-=1
                elif counter[s[right]]==-1:
                    numDifferentChar+=1

            if right-left+1==len(p): 
                if numDifferentChar==0:
                    ans.append(left)
                
                if s[left] in counter:
                    counter[s[left]]+=1
                    if counter[s[left]]==0:
                        numDifferentChar-=1
                    elif counter[s[left]]==1:
                        numDifferentChar+=1
                left+=1
        return ans

