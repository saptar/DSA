'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
'''
def getCaseChangePermutation(s:list)->list:
    if len(s)==0:
        return [""]
    r = []
    def solve(i,o):
        if i == len(s)-1:
            r.append(o)
            return
        if not s[i+1].isdigit():
            solve(i+1,o+s[i+1].upper())
            solve(i+1,o+s[i+1])
        else:
            solve(i+1,o+s[i+1])
    solve(-1,"")
    return r

        


if __name__=="__main__":
    s = list(input())
    print(getCaseChangePermutation(s))