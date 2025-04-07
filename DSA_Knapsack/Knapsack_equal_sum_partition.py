import math
def subsetSum(arr,sum,n):
    a = False
    ## base condition
    if sum == 0:
        return t[n][0]
    if n == 0:
        return t[0][sum]
    

    ## return if already seen
    if t[n][sum] != -1:
        return t[n][sum]
    
    ## choosing login
    if arr[n-1] <= sum:
        t[n][sum] = subsetSum(arr, sum - arr[n-1], n-1) or subsetSum(arr, sum, n-1)
    if arr[n-1] > sum:
        t[n][sum] = subsetSum(arr, sum, n-1)
    return t[n][sum]

def getTotalSum(arr):
    total_sum = 0
    for i in arr:
        total_sum += i
    return total_sum

if __name__ == "__main__":
    global t
    arr = list(map(int, input().split()))
    
    total_sum = getTotalSum(arr)
    t = [[-1 for j in range(math.ceil(total_sum/2) + 1)] for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(math.ceil(total_sum/2) + 1):
            if i == 0:
                t[0][j] = False
            if j == 0:
                t[i][0] = True
                
    if total_sum %2 !=0:
        print(False)
    else:
        print(subsetSum(arr,int(total_sum/2),len(arr)))

    