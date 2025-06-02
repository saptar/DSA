class TrieNode:
    def __init__(self):
        self.children = [None]*26 ## all posibility of lower case letters
        self.isEndOfWord = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word:str) ->None:
        curr = self.root
        for c in word:
            i = ord(c)-ord('a') ## get the relative position of the character starting from a
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isEndOfWord = True

    def searchWord(self, word:str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c)-ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.isEndOfWord
    
    def startsWith(self,prefix:str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c)-ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True


if __name__ == "__main__":
    trie = PrefixTree()
    trie.insert("cocomelon")
    print(trie.searchWord("watermelon"))
    print(trie.startsWith("coco"))