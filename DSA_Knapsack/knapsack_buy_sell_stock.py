'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''

def solve(arr, n, k, buy):
    ## base conditions
    if (n == 0): # no more days left.
        return 0
    if (k==0): # no more transaction left
        return 0
    if buy:
        ## we are buying
        don_take = solve(arr, n-1, k,buy)
        take = -arr[n-1] + solve(arr,n-1,k-1, False)
    else:
        ## we are selling
        don_take = solve(arr,n-1, k, buy)
        take  = arr[n-1] + solve(arr, n-1, k-1 , True)
    return max(don_take, take)


if __name__=="__main__":
    x = [7,1,5,3,6,4]
    lx = len(x)
    # k - denoting number of transactsion
    k = 2
    buy = True  ## denoting if we can buy or sell.
    print(solve(x[::-1], lx, k, buy))# inversing the array as recursion starts at the end and traversing back is not allowed.