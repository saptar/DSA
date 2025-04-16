def lcsTopDown(x, y, lx, ly):
    if ly == 0 or lx == 0:
        return t[lx][ly]
    ## choise logic
    for i in range(1,lx+1):
        for j in range(1,ly+1):
            if x[i-1] == y[j-1] and i!=j:
                t[i][j] = 1+ t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    return t[lx][ly]


if __name__=="__main__":
    x = list(input())
    y = x[::]
    len_x = len(x)
    len_y = len(y)
    global t
    t = [[-1 for j in range(len_y+1)]for i in range(len_x+1)]
    for i in range(len_x+1):
        t[i][0] = 0
    for j in range(len_y+1):
        t[0][j] = 0
    
    print(lcsTopDown(x,y,len_x,len_y))