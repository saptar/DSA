'''
Given a string such as "abc" print all the subsets of the string
eg. "", "a","ab"...
i/p:
"ab"
o/p:
"","a","b","ab"

'''
def getAllSubset(s):
    if len(s)==0:
        return ['']
    r = []
    def solve(i,o):
        if i==len(s)-1:
            r.append(o)
            return
        ## chose the element for  index
        solve(i+1,o+s[i+1])
        ## don't choose the element for index
        solve(i+1,o) 

    solve(-1,"")
    return r
if __name__ == "__main__":
    s = list(input())
    print(getAllSubset(s))