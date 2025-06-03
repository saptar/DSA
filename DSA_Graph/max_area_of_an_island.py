'''
You are given a matrix grid where grid[i] is either a 0 (representing water) 
or 1 (representing land).
An island is defined as a group of 1's connected horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.
The area of an island is defined as the number of cells within the island.
Return the maximum area of an island in grid. If no island exists, return 0.

Example:
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6
'''


def solution(grid):
    R,C = len(grid),len(grid[0])
    maxArea = float("-inf")
    directions = [(1,0),(1,0),(0,1),(0,-1)]

    def dfs(r,c):
        if min(r,c)<0 or r>=R or c>=C or grid[r][c]==0:
            return 0
        grid[r][c] = 0
        area = 1
        for dr,dc in directions:
            area += dfs(r+dr,c+dc)
        return area
    for i in range(R):
        for j in range(C):
            if grid[i][j]==1:
                maxArea = max(maxArea,dfs(i,j))
    return maxArea

if __name__=="__main__":
    grid = [
        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]
    ]
    print(solution(grid))


