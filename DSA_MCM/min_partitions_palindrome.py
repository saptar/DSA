
'''
Given a string s, the task is to find the minimum number of cuts needed for palindrome 
partitioning of the given string. A partitioning of the string is a palindrome 
partitioning if every sub-string of the partition is a palindrome.

Examples: 

Input: s = “geek” 
Output: 2 
Explanation: We need to make minimum 2 cuts, i.e., “g | ee | k”.


Input: s= “aaaa” 
Output: 0 
Explanation: The string is already a palindrome.


Input: s = “ababbbabbababa” 
Output: 3
Explanation: We need to make minimum 3 cuts, i.e., “aba | bb | babbab | aba”.


'''
def helper(s,i,j):
    if i>=j:
        return 0
    if isPalindrome(s[i:j+1]):
        return 0
    
    res = float("inf")
    for k in range(i,j):
        tmp = helper(s,i,k) + helper(s,k+1,j) + 1
        if tmp < res:
            res = tmp
    return res


def helperM(s,i,j,t):
    if i>=j:
        return 0
    if isPalindrome(s[i:j+1]):
        return 0
    if t[i][j]!=-1:
        return t[i][j]
    res = float("inf")
    for k in range(i,j):
        tmp = helperM(s,i,k,t) + helperM(s,k+1,j,t)+1
        res = min(res,tmp)
    t[i][j] = res
    return t[i][j]
    

def isPalindrome(s):
    ptr1,ptr2 = 0, len(s)-1
    while ptr1<ptr2:
        if s[ptr1]!=s[ptr2]:
            return False
        ptr1+=1
        ptr2-=1
    return True

if __name__=="__main__":
    s = str(input())
    t = [[-1 for j in range(len(s)+1)] for i in range(len(s)+1)]
    print(helper(s,0,len(s)-1))
    print(helperM(s,0,len(s)-1,t))

