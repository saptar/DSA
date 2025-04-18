
def lcs(x,y, lx, ly):
    count = 0
    if lx==0 or ly==0:
        return 0
    if x[lx-1] == y[ly-1]:
        count = 1 + lcs(x,y,lx-1,ly-1)
    else:
        count = max((lcs(x,y,lx-1,ly)),lcs(x,y,lx,ly-1))
    return count


if __name__=="__main__":
    x = list(input())
    y = list(input())
    lx = len(x)
    ly = len(y)
    count_lcs = lcs(x, y, lx, ly)
    print(lx+ly-count_lcs)