'''
Write a Java Program to generate the highest possible number by combining the elements on the inArr and display the identified largest number.

Example: inArr contains {91, 87, 63,71,54} and highest number formed is 9187716354

Input Format: 

First line denotes the size of the inArr
Second line denotes the elements present in inArr and stored in subsequent lines
Sample Input	Sample Output	Explanation
6               77568211210     The elements of inArr are arranged to get the largest number, 77568211210
10      
68
75
7
21
12		
5               9785716745	    The elements of inArr are arranged to get the largest number, 9785716745
97
85
71
67
45	

'''

if __name__ == "__main__":
    c = int(input())
    arr = list(map(str, input().split()))
    arr.sort(reverse=True)
    r_str = arr[0]
    if c==1:
        print(int(arr[0]))
    for i in range(1,c):
        place_left = r_str + arr[i]
        place_right = arr[i]+ r_str
        if (int(place_left)>int(place_right)):
            r_str = place_left
        else:
            r_str = place_right
    print(r_str)

    

    

        
        
   
            
    

