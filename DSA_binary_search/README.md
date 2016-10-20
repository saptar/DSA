## Binary Search

Binary search is a fast algorithm, as compared to linear search, which runs with time complexity  
```sh
O(n) = log n
```
This algorithm works on the principles of divide and conquer.  
A pre-requisite for this algorithm to work correctly, is to have the array sorted.

Binary Search , searches a particular item , by searching the middle element of the array.  
If a match is found , the index is returned.  
If not, then the lower or the upper bound is updated based on the fact that the search item is greater than or less than the element in the middle. This routing is followed recursively, untill the upper bound becomes less than lower bound or a match is found.  
To Calculate the midpoint following formula is used.  
```sh
midpoint = lowerBound + (upperBound - lowerBound)/2
```
If the searched item is found to be greater than the item at the midpoint then,  
```sh
lowerBound = midpoint+1;
```
Conversely, if the element at the midpoint is found to be greater than the searched element then,  
```sh
upperBound = midpoint -1 ;
```
