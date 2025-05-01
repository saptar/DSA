'''
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

'''

if __name__=="__main__":
    arr = list(map(int,input().split()))
    res = []
    part = []
    def helper(i):
        if i>=len(arr):
            res.append(part.copy())
            return
        part.append(arr[i])
        helper(i+1)
        part.pop()
        helper(i+1)
    helper(0)
    print(res)