'''
You are given an array prerequisites where prerequisites[i] = [a, b] 
indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], 
indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, 
labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. 
If there are many valid answers, return any of them. 
If it's not possible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 3, prerequisites = [[1,0]]

Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Example 2:

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

Output: []
Explanation: It's impossible to finish all courses.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.

'''
import collections
def solution(prereq,numCourses):
    ## create adj list
    adj = collections.defaultdict(list)
    for s,e in prereq:
        adj[s].append(e)
    
    courses = []
    considered = set()

    def dfs(i,visited):
        if i in visited:
            ## we have found a cycle return false
            return False
        if i in considered:
            ## we have already considered this return True
            return True
        
        visited.add(i)
        considered.add(i)
        res = True
        for dep in adj[i]:
            res = res and dfs(dep,visited)
        visited.remove(i)
        courses.append(i)
        return res
    for i in range(numCourses):
        visited = set()
        if not dfs(i,visited):
            return []
    return courses

if __name__=="__main__":
    numCourses = 3
    prereq = [[1,0]]
    print(solution(prereq,numCourses))

