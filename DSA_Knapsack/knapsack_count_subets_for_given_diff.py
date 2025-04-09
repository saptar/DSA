
def subsetCount(arr,sum,n):
    count = 0
    ## base condition
    if sum == 0:
        return 1
    if n == 0:
        return 0
    
    ## choise logic
    if arr[n-1]<=sum:
        count  = subsetCount(arr,sum - arr[n-1],n-1) + subsetCount(arr,sum, n-1)
    if arr[n-1] > sum:
        count  = subsetCount(arr,sum,n-1)
    return count 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    diff = int(input())
    n = len(arr)
    total_arr_sum = 0
    for i in arr:
        total_arr_sum+=i
    sum = int((total_arr_sum+diff)/2)
    
    print(subsetCount(arr,sum,n))