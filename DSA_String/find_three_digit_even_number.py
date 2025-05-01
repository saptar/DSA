def getCount(arr):
    count = 0
    s = set()
    new_arr = list(map(str, arr)) 
    for p,i in enumerate(new_arr):
        if i == "0":
            continue
        for q,r in enumerate(new_arr):
            if p!=q and (i,r) not in s:
                count +=1
                s.add((i,r))
    return count

    


def isEven(number):
    if number%2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    arr = list(map(int,input().split(",")))
    arr_even = list(filter(lambda x: x%2 == 0,arr))
    
    res = 0
    for i in arr_even:
        if i == 0:
            continue
        arr_copy = arr.copy()
        arr_copy.remove(i)
        
        res +=getCount(arr_copy)
    print(res)




