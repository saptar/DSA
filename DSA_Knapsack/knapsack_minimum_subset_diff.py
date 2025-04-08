

def subsetSum(arr, sum, n):
    ## base conditions
    if sum == 0:
        return t[n][0]
    if arr == 0:
        return t[0][sum]
    
    if t[n][sum] != -1:
        return t[n][sum]


    if arr[n-1] <= sum:
        t[n][sum] = subsetSum(arr, sum - arr[n-1], n-1) or subsetSum(arr,sum, n-1)
    if arr[n-1] > sum:
        t[n][sum] = subsetSum(arr, sum, n-1)
    return t[n][sum]


def subsetSumT(arr, sum, n):
    ## initialization is done in the global variable t
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[-1]



if __name__ == "__main__":
    global t
    arr = list(map(int, input().split()))
    ## get the full range of sums.
    n = len(arr)
    r = 0
    for i in arr:
        r+=i
    t = [[-1 for j in range(r+1)] for i in range(len(arr)+1)]
    
    for j in range(r+1):
        t[0][j] = False
    for i in range(n+1):
        t[i][0] = True
    
    a_sums =(subsetSumT(arr, r, len(arr)))
    p_sum = -1
    for i, sum in enumerate(a_sums):
       
       if i <= r/2 and sum:
           p_sum =  max(p_sum,i)
    print (r-2*p_sum)
        
    