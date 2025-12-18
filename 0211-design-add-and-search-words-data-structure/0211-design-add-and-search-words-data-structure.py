class WordNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = WordNode()
        
    def _walkWord(self,word):
        def dfs(index,curr_node):
            if index==len(word):
                return curr_node.is_end
            if word[index]=='.':
                for children in curr_node.children.values():
                    if dfs(index+1,children):
                        return True
                return False
            if word[index] in curr_node.children.keys():
                return dfs(index+1,curr_node.children[word[index]])
            return False

        return dfs(0,self.root)
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        result = self._walkWord(word) 
        return result