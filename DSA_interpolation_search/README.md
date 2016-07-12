## Interpolation Search

Interpolation Search is an improved variant of Binary Search.  
It works by probing position of required value.  
Pre-requisties for interpolation search to work  

- Like BS, the target array must be sorted.
- The distribution of values must be equal or linear. The interpolation search would not yeild good results if the values on which search is done are unequally distributed, e.g, exponential values.

With the above notion, interpolation search tries to probe, or do a calculated guess on the position of the searched item.
Since , the values are equally distributed, we can guess the position of searched term 'X' from the lower bound by the following euqation.  

```sh
midpoint = i + ((j-i)/(A[j]-A[i])*(X-A[i])
```
where,  
i -> lowerBound
j -> higherBound
A[i] -> element at index lowerBound
A[j] -> element at index higherBound
X -> Element to be searched.  

rest of the routine interms of updating the lowerBound and/or upperBounds in case the searched item is not found at midpoint remains same as Binary Search, a simple implementation of which can be found [here](https://github.com/saptar/DSA/tree/DSA_binary_search/DSA_binary_search).

The average case time complexity for interpolation search is found to :  
```sh
 theta(n) = log(log n)
```
and worst case(when the input is not equally distributed)  
```sh
 O(n) = n^2
```
