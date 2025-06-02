'''

Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
Constraints:

1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.


'''

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self,word:str)->None:
        curr = self.root
        for c in word:
            i = ord(c)-ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isEndOfWord = True

    def searchU(self,word:str)->bool:
        def dfs(node,w):
            if len(w) == 0:
                ##print(word," ",w," ",node.isEndOfWord)
                return node.isEndOfWord
            if not node:
                return False
            
            for c in w:
                ##print("in for loop",w)
                if c == ".":
                    ##print("children of the node",len(node.children))
                    for k in node.children:
                      if not k:
                          continue
                      if dfs(k,w[1:]):
                          return True
                else:
                    i = ord(c)-ord('a')
                    if node.children[i] == None:
                        return False
                    remainingWord = w[1:] if len(w)>0 else ""
                    ##print("else case")
                    if dfs(node.children[i],remainingWord):
                        return True
            
        return dfs(self.root,word)
                    


            
    
    def search(self,word:str)->bool:
        curr = self.root
        for c in word:
            if c == ".":
                continue
            i = ord(c)-ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.isEndOfWord if c[-1]!="." else True


if __name__=="__main__":
    inputArr = list(map(str,input().split(',')))
    WordDictionary = PrefixTree()
    res = [None]
    
    for i in range(1,len(inputArr)):
        if inputArr[i] == "addWord":
            i+=1
            res.append(WordDictionary.addWord(inputArr[i]))
        if inputArr[i] == "search":
            i+=1
            res.append(WordDictionary.searchU(inputArr[i]))
    print(res)

