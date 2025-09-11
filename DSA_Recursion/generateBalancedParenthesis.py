'''
Given n pairs of parentheses, 
write a function to generate 
all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
Constraints:
1 <= n <= 8

'''
def generateBalanceParenthesis(n:int)->list:
    if n==0:
        return [""]
    r = []
    def solve(open,closed,o):
        if open == 0 and closed == 0:
            r.append(o)
            return
        if open>0:
            solve(open-1,closed,o+"(")
        if closed>open:
            solve(open, closed-1,o+")")
    solve(n,n,"")
    return r


if __name__=="__main__":
    n = int(input())
    print(generateBalanceParenthesis(n))