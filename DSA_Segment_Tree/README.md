## Segment Tree 

Let us consider that we have an array [0...n-1] and we should be able to do the following:  
1. Find sum of the elements of the index from l to r where 0<=l<=r<=n-1  
2.Change the value of a specified element on an array to a new view.  

### Simple Solution
To calculate the sum, just run a loop from l to r and calculate the value.   
To update just arr[indexToUpdate] = value.  
The first one takes O(n) time and the update routine take O(1) time.  
Another solution would be to add up every element and save the values in another array, where the index k of the new
array would be the sum of elements from 0 to K-1 in the original array.  
For updating we need to update each element of the second array till k.  
With this approach the time take to get the sum in O(1), however the time taken to update a element in the array
would be O(n).  
Can we do better?Have both Update and sum of range running with O(logn). 

### Segment Tree Solution


![alt tag](http://d1hyf4ir1gqw6c.cloudfront.net//wp-content/uploads/segment-tree1.png)  
(image referred from [GeeksforGeeks](http://www.geeksforgeeks.org/))  
1.Leaf nodes are elements of the input array.  
2.Each internal node represents some merging of the leaf node. In this case it is sum , but can be anything.  

#### Construction of segment tree from a given array.
We start with a segment arr[0..n-1] and everytime we divide the segment into two halves untill we read a size of one.  
All levels of the constructed segment tree will be completely filled except for the last level, also the tree will be full binary tree
because the branching factor is 2.  
Since the constructed tree is always a full binary tree with n-leaves; no of internal nodes would be n-1.  
So total number of nodes would be  
```sh
2n-1
```  
Height of the tree would be log base 2 n
```sh
logn/log2
```  
For details pls visit [Geeks for geeks | segment tree](http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)


