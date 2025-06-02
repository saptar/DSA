'''
Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]
'''


def isPalindrome(s):
    ptr1, ptr2 = 0, len(s)-1
    while ptr1<ptr2:
        if s[ptr1]!=s[ptr2]:
            return False
        ptr1 +=1
        ptr2 -=1
    return True
        

if __name__=="__main__":
    s = str(input())
    res = []
    part = []
    def helper(i):
        if i>=len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if isPalindrome(substr):
                part.append(substr)
                helper(j+1)
                part.pop()
    helper(0)
    print(res)
