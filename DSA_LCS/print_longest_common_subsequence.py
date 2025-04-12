def lcs(x,y,lx,ly,res_array):
    if (lx==0 or ly==0):
        return ""
    if x[lx-1] == y[ly-1]:
        
        lcs(x,y, lx-1,ly-1,res_array)
        if x[lx-1] not in res_array:
            res_array.append(x[lx-1])
    else:
        lcs(x,y, lx-1,ly, res_array)
        lcs(x,y,lx,ly-1,res_array)
    return res_array


if __name__ == "__main__":
    x = list(input())
    y = list(input())
    lx = len(x)
    ly = len(y)
    res_array = []
    print("".join(lcs(x,y,lx,ly,res_array)))
