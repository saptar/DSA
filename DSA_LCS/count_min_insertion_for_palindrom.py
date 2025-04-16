
def lcs(x,y,lx,ly):
    t = [[-1 for j in range(ly+1)] for i in range(lx+1)]
    for j in range(ly+1):
        t[0][j] = 0
    for i in range(lx+1):
        t[i][0] = 0

    if lx == 0 or ly ==0:
        return t[lx][ly]
    for i in range(1, lx+1):
        for j in range(1, ly+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    return t[lx][ly]

if __name__=="__main__":
    x = list(input())
    y = x[::-1]
    lx = ly = len(x)
    print(lx - lcs(x,y,lx,ly)) 
    ## minimum number of insertion is same as minimum number of deletion to make it a palindrom.
    ## just reverse the input string and find the LCS.
    ## then substract the count of lcs from the size of the string.