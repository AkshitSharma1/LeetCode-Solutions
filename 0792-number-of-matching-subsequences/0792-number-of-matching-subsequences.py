class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_pos = defaultdict(list)
        for i,ch in enumerate(s): char_pos[ch].append(i)
        curr = -1
        ans = 0
        for word in words:
            curr = -1
            ok = True
            for char in word:
                index = bisect_right(char_pos[char],curr)
                if index==len(char_pos[char]):
                    ok = False
                    break
                curr = char_pos[char][index]
            if ok: ans+=1
        return ans
