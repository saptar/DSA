
def merge(arr,s,m,e):
    # copy the array into two parts left and right arrays
    L = arr[s:m+1]
    R = arr[m+1:e+1]
    # declare pointers to track left,right and the main array.
    i = 0 # to start from left most pos for L array
    j = 0 # same for R array
    k = s # where to insert in the main array
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k+=1
    ## there will either i or j which has not reached the lenght of respective Left
    ## right array, for those case, add the remaining elements directly to the end 
    ## of arr[k]
    while i<len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1

    

def mergeSort(arr,s,e):
    if e-s+1<=1:
        return arr
    m = (s+e)//2
    mergeSort(arr,s,m)
    mergeSort(arr,m+1,e)
    merge(arr,s,m,e)
    return arr


if __name__=="__main__":
    arr = list(map(int,input().split(',')))
    mergeSort(arr,0,len(arr)-1)
    print(arr)