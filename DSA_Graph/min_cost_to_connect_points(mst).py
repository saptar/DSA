'''
You are given a 2-D integer array points, where points[i] = [xi, yi]. 
Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance 
between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, 
such that there exists exactly one path between each pair of points.

Example 1:
Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

Output: 10
'''
class UnionFind:
    def __init__(self,n):
        self.parent = [None]*n
        self.rank = [None]*n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1
    def find(self, n):
        curr = self.parent[n]
        while self.parent[curr]!=curr:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2]>self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


def solution(points):
    ## use the points to create a array such as
    ## (distance,[p1,p2])
    ## where p1 and p2 are the points described by the co-ordinate
    ## distance = abs(p1x-p2x)+abs(p1y-p2y)
    arr = []
    for i in range(len(points)-1):
        for j in range(i+1,len(points)):
            distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
            arr.append((distance,[i,j]))
    ## arr provides connection between each node.
    arr.sort()
    uf = UnionFind(len(points))
    total_cost = 0
    for distance,edge in arr:
        if uf.union(edge[0],edge[1]):
            total_cost += distance
    return total_cost



if __name__=="__main__":
    points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
    print(solution(points))