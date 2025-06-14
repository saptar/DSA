'''
You are given a network of n directed nodes, labeled from 1 to n. You are also given times,
 a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal 
to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, 
representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. 
If it is impossible for all the nodes to receive the signal, return -1 instead.

Example 1:
Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

Output: 3
Example 2:

Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2

Output: -1

'''
import collections
import heapq
def findShortestTime(times,n,k):
    ## create an adjacency map
    h = collections.defaultdict(list)
    for s,e,t in times:
        h[s].append((e,t))
    
    minHeap = []
    heapq.heappush(minHeap,(0,k))
    visited = set()
    maxTime = 0

    while minHeap:
        t,n = heapq.heappop(minHeap)
        if n in visited:
            continue
        maxTime = t
        visited.add(n)
        
        for n1,t1 in h[n]:
            if n1 in visited:
                continue
            heapq.heappush(minHeap,(t+t1,n1))
    return -1 if len(visited)!=n else maxTime



if __name__=="__main__":
    times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
    n = 4
    k = 1
    print(findShortestTime(times,n,k))
