'''
Given a string s, you need to print all possible strings 
that can be made by placing spaces (zero or one) in between them
Input:
s = "ABC"
Output: (A B C)(A BC)(AB C)(ABC)
Explanation:
ABC
AB C
A BC
A B C
These are the possible combination of "ABC".
'''
def stringWithSpaces(s:list)->list:
    if len(s)==0:
        return [" "]
    r = []
    def solve(i,o):
        if i == len(s)-1:
            r.append(o)
            return
        solve(i+1,o+" "+s[i+1])
        solve(i+1,o+s[i+1])
    solve(0,s[0])
    return r

if __name__=="__main__":
    s = list(input())
    print(stringWithSpaces(s))