'''
given a stack (list on python), delete the kth element.
kth element is defined as stack.size()/2+1
eg.
1,2,3,4,5
o/p:
1,2,4,5
i/p:
1,2,3,4,5,6
o/p:
1,2,3,5,6
'''

def deleteKthElement(s:list)->list:
    if len(s)==0:
        return s
    # find k
    k = (len(s)//2) + 1
    solve(s,k)
    return s

def solve(s:list,k:int)->list:
    if k == 1:
        s.pop()
        return s
    last = s.pop()
    solve(s,k-1)
    s.append(last)
    return s
    

if __name__=="__main__":
    input_s = list(map(int, input().split(',')))
    print(deleteKthElement(input_s))