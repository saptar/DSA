

def lcs(x,y,lx,ly):
    if lx==0 or ly == 0:
        return ""
    if x[lx-1] == y[ly-1]:
        return lcs(x,y,lx-1,ly-1) + x[lx-1]
    else:
        a = lcs(x,y,lx-1,ly)
        b = lcs(x,y,lx,ly-1)
        return a if len(a) > len(b) else b
    
def lcsTopDown(x,y,lx,ly):
    t = [[-1 for j in range(ly+1)] for i in range(lx+1)]
    ## initialize
    for j in range(ly+1):
        t[0][j] = 0
    for i in range(lx+1):
        t[i][0] = 0
    
    if lx == 0 or ly == 0:
        return t[lx][ly]
    for i in range(1,lx+1):
        for j in range(1,ly+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    return t

if __name__=="__main__":
    x = list(input())
    y = list(input())
    lx = len(x)
    ly = len(y)
    #k = lcs(x,y,lx,ly)
    lcs = lcsTopDown(x,y,lx,ly)
    print(lcs)
    result = ""
    while ly > 0 or lx > 0:
        if(x[lx-1])==y[ly-1]:
            result+=x[lx-1]
            lx-=1
            ly-=1
        else:
            if lcs[lx-1][ly] > lcs[lx][ly-1]:
                result += x[lx-1]
                ly-=1
            elif lcs[lx][ly-1] > lcs[lx-1][ly]:
                result += y[ly-1]
                lx -=1
    while lx > 0:
        result += x[lx-1]
    while ly > 0:
        result += y[ly-1]
    print(result)

    