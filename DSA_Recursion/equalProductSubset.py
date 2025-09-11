'''
You are given an integer array nums containing distinct positive integers and an integer target.
Determine if you can partition nums into two non-empty disjoint subsets, with each element belonging to exactly one subset, such that the product of the elements in each subset is equal to target.
Return true if such a partition exists and false otherwise.
A subset of an array is a selection of elements of the array.
Example 1:
Input: nums = [3,1,6,8,4], target = 24
Output: true
Explanation: The subsets [3, 8] and [1, 6, 4] each have a product of 24. Hence, the output is true.
Example 2:
Input: nums = [2,5,3,7], target = 15
Output: false
Explanation: There is no way to partition nums into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.
Input
nums =
[9,1,21,6,5,23,18]
target =
207
Constraints:

3 <= nums.length <= 12
1 <= target <= 1015
1 <= nums[i] <= 100
All elements of nums are distinct.

'''
from functools import reduce
from operator import mul
def isSubsetPossible(arr:list,target:int)->bool:
    if len(arr)==0 or target==0:
        return False
    checkArr = [False for _ in range(len(arr))]
    product = reduce(mul,arr)
    if product != target**2:
        return False
    ans = False
    c = 0
    def solve(i,o):
        if o==target:
            nonlocal c
            c = c+1
            return
        if i == len(arr)-1 or o>target:
            return
        if target%arr[i+1] == 0 and not checkArr[i+1]:
            checkArr[i+1]=True
            solve(i+1,o*arr[i+1])
            checkArr[i+1] = False
            solve(i+1,o)
        else:
            solve(i+1,o)
    solve(-1,1)
    
    if c>=2:
        ans = True
    return ans
    



if __name__=="__main__":
    arr = list(map(int, input().split(',')))
    target = int(input())
    print(isSubsetPossible(arr,target))