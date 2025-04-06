

def branch_and_bound(n,wmax, items):
    w_arr = []
    v_arr = []
    for i in items:
        a,b = i
        w_arr.append(a)
        v_arr.append(b)
    return topdown_knapsack(w_arr,v_arr,wmax,n)

def topdown_knapsack(w_arr,v_arr,wmax,n):
    # initialize the array
    t = [[-1 for j in range(wmax+1)] for i in range(n+1)]
    # set the base conditions
    for i in range(n+1):
        for j in range(wmax+1):
            if i==0 or j==0:
                t[i][j] =0
    
    for i in range(1,n+1):
        for j in range(1,wmax+1):
            if(w_arr[i-1]<=j): ## the current weight is less than the wmax for the subproblem
                t[i][j] = max((v_arr[i-1] + t[i-1][j - w_arr[i-1]]),t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    
    return t[n][wmax]




if __name__ == "__main__":
    n, wmax = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]

    print(branch_and_bound(n, wmax, items))