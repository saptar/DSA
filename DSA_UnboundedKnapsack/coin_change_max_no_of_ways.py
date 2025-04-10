def maxNoOfWays(arr, sum, n):
    count = -1
    ## base condition
    if sum == 0:
        return 1
    if n == 0:
        return 0
    
    ## choise logic
    if arr[n-1] <= sum:
        count = maxNoOfWays(arr, sum - arr[n-1], n) + maxNoOfWays(arr,sum,n-1)
    if arr[n-1] > sum:
        count  = maxNoOfWays(arr, sum, n-1)

    return count

def maxNoOfWaysT(arr, sum, n):
    for j in range(sum+1):
        t[0][sum] = 0
    for i in range(n+1):
        t[i][0] = 1
    ## choise logic
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                t[i][j] = t[i][j-arr[i-1]] + t[i-1][j]
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
    return t[n][sum]



if __name__=="__main__":
    arr = [1,2,3]
    sum = 5
    n = len(arr)
    global t
    t = [[0 for j in range(sum+1)] for i in range(n+1)]
    

    print(maxNoOfWays(arr,sum,n))
    print(maxNoOfWaysT(arr, sum, n))