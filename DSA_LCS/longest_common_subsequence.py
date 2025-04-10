
def lcs(x,y,lx,ly):
    if lx==0 or ly==0:
        return t[lx][ly]
    ## choise diagram
    if (x[lx-1] == y[ly-1]):
        t[lx][ly] = 1 + lcs(x,y, lx-1, ly-1)
    else:
        t[lx][ly] = max((lcs(x,y,lx-1,ly)),(lcs(x,y,lx,ly-1)))
    return t[lx][ly]


def lcsTopDown(x, y, lx, ly):
    if ly == 0 or lx == 0:
        return t[lx][ly]
    ## choise logic
    for i in range(1,lx+1):
        for j in range(1,ly+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1+ t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    return t[lx][ly]


if __name__=="__main__":
    x = list(input())
    y = list(input())
    len_x = len(x)
    len_y = len(y)
    global t
    t = [[-1 for j in range(len_y+1)]for i in range(len_x+1)]
    for i in range(len_x+1):
        t[i][0] = 0
    for j in range(len_y+1):
        t[0][j] = 0
    print(lcs(x, y, len_x,len_y))
    print(lcsTopDown(x,y,len_x,len_y))