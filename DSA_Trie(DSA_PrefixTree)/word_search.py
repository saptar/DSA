'''
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word 
with a path in the board with horizontally or vertically neighboring cells. 
The same cell may not be used more than once in a word.

Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]

Constraints:

1 <= board.length, board[i].length <= 10
board[i] consists only of lowercase English letter.
1 <= words.length <= 100
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.

'''

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        curr = self.root
        for c in word:
            i=ord(c)-ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()

            curr = curr.children[i]
        curr.isEndOfWord = True

def findWords(board,words):
    R,C = len(board),len(board[0])
    w,res = set(),set()
    t = []
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    pt = PrefixTree()
    def dfs(r,c,p):
        if p and p.isEndOfWord:
            res.add("".join(t.copy()))
            
        
        i = ord(board[r][c]) - ord('a')
        if p.children[i]:
            w.add((r,c))
            t.append(board[r][c])
            for dr,dc in directions:
                if min(r+dr,c+dc)<0 or (r+dr)>=R or (c+dc)>=C or (r+dr,c+dc) in w:
                    continue
                dfs(r+dr,c+dc,p.children[i])
            w.remove((r,c))
            t.pop()
        return
    def createPrefixTree(words):
        for word in words:
            pt.addWord(word)
    createPrefixTree(words)
    for i in range(R):
        for j in range(C):
            dfs(i,j,pt.root)
    return res
            

if __name__=="__main__":
    board = [["a","b","c","d"],["s","a","a","t"],["a","c","k","e"],["a","c","d","n"]]
    words = ["bat","cat","back","backend","stack"]
    print(list(findWords(board,words)))