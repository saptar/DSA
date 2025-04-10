import sys

def minNoOfCoins(arr, sum, n):
    count = -1
    ## base condition
    if sum == 0:
        return 0
    if (n == 0 and sum!=0):
        return sys.maxsize
    if (n == 1):
        return sum
    ## choise logic
    if arr[n-1] <= sum:
        count = min((1+ minNoOfCoins(arr, sum - arr[n-1],n)),minNoOfCoins(arr, sum, n-1))
    if arr[n-1] > sum:
        count  = minNoOfCoins(arr, sum, n-1)
    return count

def coinChangeMem(arr, sum, n):
    if sum == 0:
        return t[n][0]
    if n == 0 and sum!=0:
        return t[0][sum]
    if n == 1:
        return t[1][sum]
    if t[n][sum] !=-1:
        return t[n][sum]
    if arr[n-1] <= sum:
        t[n][sum] = min((1+ coinChangeMem(arr, sum - arr[n-1],n)), coinChangeMem(arr, sum, n-1))
    if arr[n-1] > sum:
        t[n][sum] = coinChangeMem(arr, sum, n-1)
    return t[n][sum]




if __name__ == "__main__":
    arr=list(map(int, input().split()))
    sum = int(input())
    n = len(arr)
    global t
    t = [[-1 for j in range(sum+1)]for i in range(n+1)]
    for i in range(n+1):
        t[i][0] = 0
    for j in range(sum+1):
        if(j!=0):
            t[0][j] = sys.maxsize
            if(j%arr[0]==0):
                t[1][j]=int(j/arr[0])
            else:
                t[1][j] = sys.maxsize
    print(coinChangeMem(arr, sum, n))
    
    print(minNoOfCoins(arr, sum, n))