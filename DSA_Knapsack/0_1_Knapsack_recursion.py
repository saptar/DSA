import heapq
import sys

infinity = sys.maxsize


def branch_and_bound(n, wmax, items):
    # Write the code here
    global t
    w_arr = []
    v_arr = []
    for i in items:
        a,b = i
        w_arr.append(a)
        v_arr.append(b)
    t = [[-1 for j in range(wmax+1)] for i in range(n)]
    
    return get_max_value(w_arr,v_arr,wmax,n-1)
        

def get_max_value(w_arr,v_arr,wmax,n):
    max_value = -1
    
    
    if(wmax == 0 or n == 0):
        return 0
    if t[n][wmax] != -1:
        return t[n][wmax]
        
    if w_arr[n] <= wmax:    
        t[n][wmax] = max((v_arr[n] + get_max_value(w_arr,v_arr,wmax - w_arr[n],n-1)),get_max_value(w_arr,v_arr,wmax,n-1))
    if w_arr[n] > wmax:
        t[n][wmax] = get_max_value(w_arr,v_arr,wmax,n-1)
    return t[n][wmax]

if __name__ == "__main__":
    n, wmax = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]

    print(branch_and_bound(n, wmax, items))
