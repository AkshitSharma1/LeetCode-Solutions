class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_index_map ={k:i for i,k in enumerate(order)}
        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]
            n,m = len(word1),len(word2)
            p1,p2 = 0,0
            while p1<n and p2<m and word1[p1]==word2[p2]:
                p1+=1
                p2+=1
            if p1==n and p2==m:
                continue
            elif p1<n and p2==m:
                return False
            elif p1==n and p2<m:
                continue
            else:
                #when both p1 < n and p2<m
                if char_to_index_map[word1[p1]]>char_to_index_map[word2[p2]]:
                    return False
        return True

