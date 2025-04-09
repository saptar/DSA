def getMaxPrice(arr_cut, arr_price, sum, n):
    maxPrice = -1
    ## initial conditions
    if sum == 0:
        return 0
    if n == 0:
        return 0
    
    ## choise logic
    if arr_cut[n-1] <= sum:
        maxPrice = max((arr_price[n-1] + getMaxPrice(arr_cut,arr_price,sum - arr_cut[n-1],n)),
                       getMaxPrice(arr_cut, arr_price,sum,n-1))
    if arr_cut[n-1] > sum:
        maxPrice = getMaxPrice(arr_cut, arr_price, sum, n-1)
    return maxPrice

def getMaxPriceMem(arr_cut, arr_price, sum, n):
    if sum == 0:
        return t[n][0]
    if n == 0:
        return t[0][sum]
    
    if t[n][sum] != -1:
        return t[n][sum]
    ## choise logic
    if arr_cut[n-1] <= sum:
        t[n][sum] = max((arr_price[n-1] + getMaxPrice(arr_cut,arr_price,sum - arr_cut[n-1],n)),
                       getMaxPrice(arr_cut, arr_price,sum,n-1))
    
    if arr_cut[n-1] > sum:
        t[n][sum] = getMaxPrice(arr_cut, arr_price, sum, n-1)
    return t[n][sum]


if __name__=="__main__":
    arr_price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 8
    arr_cut = [i for i in range(1,9)]
    global t 
    t = [[-1 for j in range(n+1)] for i in range(n+1) ]
    for i in range(n+1):
        t[0][i] = 0
        t[i][0] = 0
    print(getMaxPrice(arr_cut,arr_price,n,n))
    print(getMaxPriceMem(arr_cut,arr_price,n,n))