def lcs(x,y,lx,ly):
    if lx==0 or ly==0:
        return ""
    if x[lx-1] == y[ly-1]:
        return lcs(x,y,lx-1,ly-1) + x[lx-1]
    else:
        arr1 = lcs(x,y,lx-1,ly)
        arr2 = lcs(x,y,lx,ly-1)
        return arr1 if len(arr1) > len(arr2) else arr2






if __name__=="__main__":
    x = list(input())
    y = list(input())
    lx = len(x)
    ly = len(y)
    o_arr = lcs(x,y,lx, ly)
    insertion = deletion = 0
    for i in x:
        if i not in o_arr:
            deletion+=1
    for j in y:
        if j not in o_arr:
            insertion+=1
    print (str(insertion)," ",str(deletion))
