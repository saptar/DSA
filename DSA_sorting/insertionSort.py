def insertionSort(arr):
    lengthOfArr = len(arr)
    for i in range(1,lengthOfArr):
        j = i-1
        while (j>=0 and arr[j]>arr[j+1]):
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j -=1
    return arr


if __name__=="__main__":
    input_arr = list(map(int,input().split(',')))
    sorted_arr = list(insertionSort(input_arr))
    print(sorted_arr)
