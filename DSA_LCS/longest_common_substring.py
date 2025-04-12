

def LCSubstring(x,y,lx,ly):
    print("LCSubstring("+str(lx)+","+str(ly)+")")
    ## base condition
    if lx==0 or ly == 0:
        return 0
    ## choise condition
    if x[lx-1] == y[ly-1]:
        
        count = 1+ LCSubstring(x,y, lx-1, ly-1)
        
    else:
       
        count = 0
    print(str(count)," "+str(lx)+" "+str(ly))
        #count = max((LCSubstring(x,y,lx-1,ly)),LCSubstring(x,y,lx,ly-1))
    return max(count,max((LCSubstring(x,y,lx-1,ly)) ,( LCSubstring(x,y,lx,ly-1))))



def longest_common_substring_count(x, y):
    def recursive_lcs(i, j, count):
        # Base case: If either string is exhausted
        if i < 0 or j < 0:
            return count
        
        # If characters match, increment the count and continue
        if x[i] == y[j]:
            count = recursive_lcs(i - 1, j - 1, count+1)
        
        # Explore other possibilities by resetting the count
        count1 = recursive_lcs(i - 1, j, 0)
        count2 = recursive_lcs(i, j - 1, 0)
        
        # Return the maximum count among all possibilities
        return max(count, count1, count2)

    # Start recursion from the last indices of both strings
    return recursive_lcs(len(x) - 1, len(y) - 1, 0)


if __name__=="__main__":
    x = list(input())
    y = list(input())
    len_x = len(x)
    len_y = len(y)
    print(longest_common_substring_count(x,y))
    #print(LCSubstring(x,y, len_x,len_y))