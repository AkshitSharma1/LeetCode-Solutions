class TrieNode():
    def __init__(self):
        self.pass_count = 0
        self.end_count = 0
        self.children = dict()
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._size = 0

    def insert(self,word):
        node = self.root
        node.pass_count+=1
        self._size+=1
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.pass_count+=1
        node.end_count+=1
    
    def _walk(self,word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return None
        return node
    
    def common_prefix(self):
        #will return the longest prefix
        prefix = []
        node = self.root
        while node and len(node.children)==1 and node.end_count==0:
            (char,child), = node.children.items()
            prefix.append(char)
            node = child
        return "".join(prefix)
    


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs: trie.insert(word)
        return trie.common_prefix()
       