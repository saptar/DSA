


def lcs(x,y,lx,ly):
    if (lx==0 or ly==0):
        return ""
    if x[lx-1] == y[ly-1]:
        
        return lcs(x,y, lx-1,ly-1) + x[lx-1]
        
    else:
        
        lcs1= lcs(x,y, lx-1,ly)
        lcs2 = lcs(x,y,lx,ly-1)
        return lcs1 if len(lcs1)>len(lcs2) else lcs2
    return res_array


if __name__ == "__main__":
    x = list(input())
    y = list(input())
    lx = len(x)
    ly = len(y)
    res_array = []
    print("".join(lcs(x,y,lx,ly)))
