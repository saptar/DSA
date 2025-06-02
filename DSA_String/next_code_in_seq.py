'''
Mat manages Livingston Library. He uses a unique numbering pattern for books gifted by the members. Each book will have a unique alphabet sequence followed by a 4-digit numeric sequence.

Alphabet sequence: A,B…Z, AA, AB…ZZ, AAA…ZZZ…

Number Sequence: 0001 to 9999

Sample Book ID: A0001, A0002,…..,A9999, B0001,….Z9999,AA0001....ZZ9999,...

Given the last generated book ID and the number of new books gifted by the members, write a program to print the book IDs.

Input format:

The first line contains the last generated book ID and the second line contains the number of new books. Read the input from standard input stream.

Output format:

Print the generated book IDs separated by comma to the standard output stream

Sample Input	Sample Output	Explanation
A0001
5	A0002,A0003,A0004,A0005,A0006	undefined
Z9998
5	Z9999,AA0000,AA0001,AA0002,AA0003	undefined
ZZZ9998
5	ZZZ9999,AAAA0000,AAAA0001,AAAA0002,AAAA0003	undefined
Languages: Python 3,C#,Java,C++,C,Scala,Go,Perl,Bash,Plain JavaScript,R,PHP,Ruby,Python,Clojure

'''
import string

def getNextCode(lastCode):
    
    arr_alpha = [i for i in list(lastCode) if i in string.ascii_uppercase]
    arr_num = [int(i) for i in list(lastCode) if i in [str(j) for j in range(10)]]
    
    carry = 0
    l_arr_alpha = len(arr_alpha)
    
    num_add = int(''.join(map(str,arr_num)))+1
    
    ret_num = ""
    ret_alpha = ""
    if num_add > 9999:
        ret_num = "0000"
        carry = 1
    else:
        tmp = 0
        if len(str(num_add))<4:
            tmp = 4- len(str(num_add))
        ret_num ="0"*tmp +  str(num_add)
        carry = 0
    
    counter = -1
    while l_arr_alpha > 0:
        if ord(arr_alpha[counter])+ carry > 90:
            ret_alpha +="A"
            carry = 1
        else:
            ret_alpha += chr(ord(arr_alpha[counter])+carry)
            carry = 0
        l_arr_alpha -=1
        counter -=1
    if carry == 1:
        ret_alpha+="A"
    
    
    return ret_alpha[::-1]+str(ret_num)






if __name__=="__main__":
    c = int(input())
    last_code = str(input())
    
    next_codes = []
    while c>0:
        
        next_code = getNextCode(last_code)
        next_codes.append(next_code)
        last_code = next_code
        c-=1
    print(next_codes)
