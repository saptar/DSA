
def mcm(arr, i, j):
    if i>=j:
        return 0 ## subproblems overlapping on if i==j meaning only one array in parenthesis
    ans = float("inf")
    for k in range(i,j):
        tempAns = mcm(arr,i,k) + mcm(arr, k+1,j) + arr[i-1]*arr[k]*arr[j]
        ans = min(tempAns,ans)
    return ans


if __name__=="__main__":
    x = list(map(int,input().split()))
    lx = len(x)
    print(mcm(x,1,lx-1))