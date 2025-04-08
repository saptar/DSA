
def countSubset(arr, sum, n):
    
    ## base condition
    if sum == 0:
        return t[n][0]
    if n==0 : 
        return t[0][sum]
    
    if t[n][sum] != -1:
        return t[n][sum]

    
    ## choise login
    if arr[n-1] <= sum:
        t[n][sum] = countSubset(arr, sum- arr[n-1], n-1) + countSubset(arr, sum, n-1)
    if arr[n-1] > sum:
        t[n][sum]  = countSubset(arr,sum,n-1)
    return t[n][sum]


if __name__ == "__main__":
    global t
    arr = list(map(int,input().split()))
    n = len(arr)
    sum = int(input())
    t = [[-1 for j in range(sum+1)] for i in range(n+1)]
    for j in range(sum+1):
        t[0][j] = 0
    for i in range(n+1):
        t[i][0] = 1
    print(countSubset(arr, sum, n))
