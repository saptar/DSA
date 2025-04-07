def subsetSum(arr,sum,n):
    ## base condition
    if sum == 0:
        return t[n][0]
    if n==0:
        return t[0][sum]
    if t[n][sum] != -1:
        return t[n-1][sum-1]
    ## recursive logic
    if arr[n-1] > sum:
        t[n][sum] = subsetSum(arr,sum,n-1)
    if arr[n-1] <= sum:
        t[n][sum] = subsetSum(arr,sum-arr[n-1],n-1) or subsetSum(arr,sum,n-1)
    return t[n][sum]


if __name__=="__main__":
    input_arr = list(map(int, input().split()))
    sum = int(input())
    global t
    t = [[-1 for j in range(sum+1)] for i in range(len(input_arr)+1)]
    for i in range(len(input_arr)+1):
        for j in range(sum+1):
            if i==0:
                t[0][j] = False
            if j == 0:
                t[i][0] = True        
    print (subsetSum(input_arr,sum,len(input_arr)))

