'''
Given a 2D grid grid where '1' represents land and '0' represents water, 
count and return the number of islands.

An island is formed by connecting adjacent lands horizontally 
or vertically and is surrounded by water. 
You may assume water is surrounding the grid 
(i.e., all the edges are water).
Example:
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4


'''

def solution(grid):
    R,C = len(grid),len(grid[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    islands = 0
    def dfs(r,c):
        
        if grid[r][c] == "0":
            return
       
        grid[r][c] = "0"
        for dr,dc in directions:
            if min(r+dr,c+dc)<0 or (r+dr)>=R or (c+dc)>=C or grid[r+dr][c+dc]=="0":
                continue
            dfs(r+dr,c+dc)
        return
            
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "1":
                islands+=1
                dfs(i,j)
    
    
    return islands

if __name__=="__main__":
    grid = [
        ["1","1","1","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(solution(grid))
