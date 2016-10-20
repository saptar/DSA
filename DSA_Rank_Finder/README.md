## Kth largest/smallest element in an unsorted array.

The idea is to find the element bearing a given rank in an array in linear time.
Rank of an element is defined to be the position of an element in a sorted array.  
The naive approach would be to simply apply **Heap sort** or **Merge Sort** on a given array and  
get the resultant sorted array from which the element bearing rank k can be obtained in unit time.  

However, the time complexity of such an exercise would be  
```sh
O(n) = nlogn
```

Can we do better? YES  
The associated code is representation of one such routine where once can find the element bearing  
rank k in linear time. The same principle can be used to find the _median_ to partition the array  
for __Quick Sort__, which then guarantees a worst case time complexity of
```sh
O(n) = nlogn
```
 way better than
```sh
O(n) = n^2
```
#### RankFinder: Expected linear time

In the routine where we use randomised partition is an algorith with an expected linear time complexity,  
however the worst case can still be  
```sh
O(n) = n^2
```  
As the randomizer can return a value which is the last element in the array.

#### RankFind : worst case linear time

