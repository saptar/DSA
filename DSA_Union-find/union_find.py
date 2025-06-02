class UnionFind:
    
    def __init__(self,n):
        self.parent = {}
        self.rank = {}
        for i in range(1,n+1):
            ## initialize all the node to have itself as parent
            ## initialize rank of all nodes to be 1
            self.parent[i] = i
            self.rank[i] = 1
    def find(self,n):
        # this method helps to find the parent of the given node n
        # using path compression, here the parent of node n would be
        # the root of the component that n belongs to
        if n!=self.parent[n]:
            # the node does not have itself as parent
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        ## this method takes in two vertises or nodes
        ## and tries to union them.
        ## if they cannot be unionized since the share the same
        ## parent return False.
        ## else depending on range of the vertices, join them and return True.
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            ## the are part of the same component
            return False
        if self.rank[n1] > self.rank[n2]:
            self.parent[n2] = n1
        elif self.rank[n2] > self.rank[n1]:
            self.parent[n1] = n2
        else:
            ## they are of equal rank
            ## make n2 the parent of n1 and increment the rank of n2
            self.parent[n1] = n2
            self.rank[n2] +=1
        return True


if __name__ == "__main__":
    edges = [[1,2],[4,1],[2,4]]
    ## this represents a graph with cycle
    n=4
    uf = UnionFind(n)
    for n1,n2 in edges:
        if not uf.union(n1,n2):
            print('cycle found for the edge',(n1,n2))
            break
        print('no cycle found',(n1,n2))
        
        

