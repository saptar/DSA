'''
You are given a 
m×n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. 
We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. 
If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
'''

from collections import deque
def solution(grid):
    R,C = len(grid),len(grid[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    d = deque()
    visited = set()
    distance = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                ## trasure chest location
                d.append((i,j))
                visited.add((i,j))
    
    while d:
        l = len(d)
        while l>0:
            r,c = d.popleft()
            grid[r][c] = distance
            for dr,dc in directions:
                if min(r+dr,c+dc)<0 or (r+dr)>=R or (c+dc)>=C or grid[r+dr][c+dc]==-1 or (r+dr,c+dc) in visited:
                    continue
                d.append((r+dr,c+dc))
                visited.add((r+dr,c+dc))
            l-=1
        distance+=1

if __name__=="__main__":
    grid = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]
    solution(grid)
    print(grid)

                


    