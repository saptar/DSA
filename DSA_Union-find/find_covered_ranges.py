'''
you are given a graph with n nodes.Initially, the graph is disconnected,meaning it has 0 edges

each node has value written on it such that ith node has value i

we say that a range [l,r] is covered in a set s, if for each i from l to r, i appears in s.

Now let's define beauty(s), as the minimum number of covered ranges such that each element of s 
belong to one of these ranges. 
so beauty([1,2,4,5,8,11]) = 4 where covered ranges are [1,2],[4,5],[8,8],[11,11]

You have to process two types of queries:
type 1 - 1, i, j : create a edge between i and j
type 2: - 2,u,0 : find number of covered ranges in the connected component u.


'''





import sys
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        # Each node initially covers only itself
        self.intervals = {i: [(i, i)] for i in range(1, n + 1)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def _add_interval(self, merged, interval):
        if not merged:
            merged.append(interval)
        else:
            last = merged[-1]
            # If current interval overlaps or is adjacent to last, merge them
            if interval[0] <= last[1] + 1:
                merged[-1] = (last[0], max(last[1], interval[1]))
            else:
                merged.append(interval)

    def merge_intervals(self, list1, list2):
        merged = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i][0] < list2[j][0]:
                self._add_interval(merged, list1[i])
                i += 1
            else:
                self._add_interval(merged, list2[j])
                j += 1
        # Add remaining intervals
        while i < len(list1):
            self._add_interval(merged, list1[i])
            i += 1
        while j < len(list2):
            self._add_interval(merged, list2[j])
            j += 1
        return merged

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            # Union by size heuristic
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]
            # Merge intervals of b into a
            self.intervals[a] = self.merge_intervals(self.intervals[a], self.intervals[b])
            del self.intervals[b]

    def get_covered_ranges(self, x):
        root = self.find(x)
        return self.intervals[root]


def get_ans(n, q, t, queries):
    dsu = DSU(n)
    c=0
    for i,u,v in queries:
        if i == 1:
            dsu.union(u,v)
        else:
            p=dsu.get_covered_ranges(u)
            c+=len(p)
    return c
        



def main():
    n = int(sys.stdin.readline().strip())
    
    q = int(sys.stdin.readline().strip())
    
    t = int(sys.stdin.readline().strip())
    
    queries = []
    for _ in range(q):
        queries.append(list(map(lambda x: int(x), sys.stdin.readline().strip().split(" "))))

    result = get_ans(n, q, t, queries)

    print(result)


if __name__ == "__main__":
    main()