def lcs(x,y,lx,ly):
    if lx==0 or ly==0:
        return 0
    if x[lx-1] == y[ly-1]:
        return 1 + lcs(x,y,lx-1,ly-1)
    else:
        return max((lcs(x,y,lx-1,ly)),lcs(x,y,lx,ly-1))

if __name__=="__main__":
    x = list(input())
    y = x[::-1]
    lx = ly = len(x)
    print(lx-lcs(x,y,lx,ly))