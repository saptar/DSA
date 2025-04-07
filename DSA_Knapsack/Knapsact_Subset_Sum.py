def subsetSum(arr,sum,n):
    a = False
    ## base condition
    if sum == 0:
        return True
    if n==0:
        return False
    ## recursive logic
    if arr[n-1] > sum:
        a = subsetSum(arr,sum,n-1)
    if arr[n-1] <= sum:
        a = subsetSum(arr,sum-arr[n-1],n-1) or subsetSum(arr,sum,n-1)
    return a


if __name__=="__main__":
    input_arr = list(map(int, input().split()))
    sum = int(input())
    print (subsetSum(input_arr,sum,len(input_arr)))

