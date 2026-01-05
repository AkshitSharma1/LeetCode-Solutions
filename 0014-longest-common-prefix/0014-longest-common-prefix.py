class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        pointers = [0 for _ in range(n)]
        strs.sort()
        for i,curr_char in enumerate(strs[0]):
            for other_string in strs[1:]:
                if curr_char!=other_string[i]:
                    return strs[0][:i]
        return strs[0]