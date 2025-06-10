'''
You are given an array prerequisites where prerequisites[i] = [a, b] 
indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, 
labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, 
otherwise return false.

Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]

Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false
Explanation: In order to take course 1 you must take course 0, 
and to take course 0 you must take course 1. So it is impossible.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.


'''
import collections
def solution(prereq,numCourses):
    ## we use topological sort with a hashset containing
    ## visited node for a particular dfs path
    ## if we come across the same node twice while traversing DFS
    ## from a given starting point, we return false

    ## create adj list
    adj = collections.defaultdict(list)
    for s,e in prereq:
        adj[s].append(e)

    def dfs(i,visited):
        if i in visited:
            return False
        visited.add(i)
        res = True
        for dep in adj[i]:
            print(f'inside for loop {dep}')
            res = res and dfs(dep,visited)
        visited.remove(i)
        return res

    for i in range(numCourses):
        visited = set()
        if not dfs(i,visited):
            return False
    return True

    
    




if __name__=="__main__":
    prereq = [[0,1]]
    numCourses = 2
    print(solution(prereq,numCourses))
