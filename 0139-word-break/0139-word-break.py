class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._size = 0
    
    def insert(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)        

        @lru_cache(maxsize=512)
        def can_segment(index):
            nonlocal s
            n = len(s)
            if index>=n: return True
            curr_node = trie.root
            for i in range(index,n,1):
                if s[i] not in curr_node.children: return False
                curr_node = curr_node.children[s[i]]
                if curr_node.is_end and can_segment(i+1): return True
            return False

        return can_segment(0)
                
        