class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.isEnd
            
            if word[i] != '.':
                if word[i] not in node.children:
                    return False
                return dfs( i + 1, node.children[word[i]])
            
            else:
                for n in node.children.values():
                    if dfs(i + 1, n):
                        return True
                
                return False

        return dfs(0, self.root)
        
