
from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words[0])
        k = len(words)
        ans = []

        if m*k>n: return ans

        for offset in range(m):
            count = Counter(words)
            l = offset

            for r in range(offset,n-m+1,m):
                word = s[r:r+m]
                count[word]-=1

                while count[word]<0:
                    count[s[l:l+m]]+=1
                    l+=m

                if l>r:
                    del count[word]

                if r-l+m==m*k:
                    ans.append(l)

        return ans
