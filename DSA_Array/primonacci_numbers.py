'''
given a starting number and ending number
find if the fibonacci number falling between the given limit
is a prime number
return all such prime numbers
e.g
start=10; end=50
return [2,3,5,13]

'''
def getFibonacciNumber(n,arr):
    #  1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    if(n<=1):
        
        return 1
    
    n = getFibonacciNumber(n-1,arr) + getFibonacciNumber(n-2,arr)
    if n not in arr:
        arr.append(n)
    return n


if __name__=="__main__":
    s= int(input())
    e = int(input())
    arr = [1,1]
    getFibonacciNumber(10,arr)
    print(arr)
    #res = getPrimes(arr)