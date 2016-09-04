## Sorting Techniques

Sorting refers to arranging data in a particular format.  
Sorting algorithms specify ways to arrange data in a particlar order, the most common being numerical or lexicographical.  

### Types of sorting

There are certain types of sorting , with respect to the memory utilisation and original order preservation etc  
- In place sorting and Not in place sorting  
	Certain algorithms may need to allocate extra space in terms of a new variable to hold temporary values or to use it in a way that facilitates comparisions. Such algorithms that might use space equal to or more the number of elements that are being sorted are referred to as *NOT IN PLACE* sorting and conversely the algorithms which does not require additional memory space are referred to as *IN PLACE* sorting algorithms. Bubble sort can be an example of in-place sorting where as merge sort can be an example of not-in-place sortingf algorithms.  

- Stable and Not Stable sorting  
	If a sorting algorithm, after sorting the contents, does not change the sequence of similar content in which they appear, it is called a *STABLE* sorting algorithm and converse the ones which do change the original sequence of similar contents are said to be *NOT STABLE* algorithms.  

- Adaptive and Non Adaptive sorting  
	If a sorting algorithm takes the advantage of already sorted elements in the given list, it is known as *ADAPTIVE* sorting algorithm and coversely , if an algorithm does not take such an advantage, it is called *NON ADAPTIVE* algorithm.  

### Well known sorting algorithms.

As a part of this exercise, we would be looking into the implementation of the following well know sorting algorithms:  

- Bubble Sort  
- Insertion Sort  
- Selection Sort  
- Merge Sort  
- Shell Sort  
- Quick Sort  

#### Bubble Sort

Bubble sort is a simple where adjacent pair of elements are compared and if the order is not as per desired(ascending or descending), then swap the element or else keep it as it is. When such an algorithm moves over the list once, we would end up getting the largest value at the last index/position of the list. The algorithm stops when for a pass over the entire list, no swaps are made.  
The worst case and average case time complexity:  
```sh
T(n) = O(n^2)
```

#### Insertion Sort

This is a in-place comparision based algorithm. Here a sublist is maintained which is always sorted. A element which is to be 'insert'ed in this sorted sub-list, has to find its appropriate place and insert it there. The array is searched sequentially and unsorted items are moved and inserted into sorted sub-list (in the same array). This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n are no. of items.  

Simple Algorithm for insertion sort  
```sh
Step 1 − If it is the first element, it is already sorted. return 1;
Step 2 − Pick next element
Step 3 − Compare with all elements in the sorted sub-list
Step 4 − Shift all the elements in the sorted sub-list that is greater than the value to be sorted
Step 5 − Insert the value
Step 6 − Repeat until list is sorted
```

#### Selection Sort

This sorting algorithm is a in-place comparsion based algorithm, in which the list is divided into two parts , the sorted part at the left end and the unsorted part at the right end. Initially sorted part is empty and unsorted part is the entire list. For the first position, in the sorted list, we scan the entire right end and find out the lowest value element and place it in the first position. Followed by second one and so on.  
Selection sort is an unstable sorting algorithm as the sequence of similar valued elements is not guaranteed to be maintained after sorting of the array.  
The time complexity for this techinque is  
```sh
T(n) = O(n2)
```
Step wise algorithm  
```sh
Step 1 − Set MIN to location 0
Step 2 − Search the minimum element in the list
Step 3 − Swap with value at location MIN
Step 4 − Increment MIN to point to next element
Step 5 − Repeat until list is sorted
```

#### Merge Sort

Merge sort is based on divide and conquer technique. It divides an array into halves and then combines them in a sorted manner.

Algorithm for merge sort  
```sh
Step 1 − if it is only one element in the list it is already sorted, return.
Step 2 − divide the list recursively into two halves until it can no more be divided.
Step 3 − merge the smaller lists into new list in sorted order.
```

The worst time complexity of merge sort is
```sh
T(n) = O(nlogn)
```
which is significantly better than the previous sorting techniques.

#### Shell Sort

Shell sort is an highly efficient algorithm base on insertion sort. This algorithm avoids large shifts as in case of insertion sorts if the smaller value is far right and has to move far left.  
This algorithm uses insertion sort on widely spread elements first to sort them and then sorts the less widely spaced elements. This spacing is termed as interval and the interval is calculated based on Knuth's formula as 
```sh
h = h*3 +1
```
where h is interval with inital value of 1  
Algorithm
```sh
Step 1 − Initialize the value of h
Step 2 − Divide the list into smaller sub-list of equal interval h
Step 3 − Sort these sub-lists using insertion sort
Step 3 − Repeat until complete list is sorted
```

This algorithm has average and worst case time complexity of O(n). However, this is dependent on the selected interval and the distribution of values. For more details please visit [wikipedia](https://en.wikipedia.org/wiki/Shellsort) page on shell sort. It is rarely used physical applications for an inproper value of interval may increase time complexity. However, certain networking applications does make use of shell sort.

#### Quick Sort

Quick sort is a highly efficient algorithm based on partitioning array into two parts, it is a divide and conquer algorithm. A large array is partioned into two parts one which holds values smaller than the pivot value on which the partition is made and another array holds the value greater than then pivot value.  
The quick sort partitions the array and then calls itself recursive twice to sort the two sub arrays, much like the merge sort.  
This algorithm is quite efficient for medium and large data sets with time complexity of
```sh
T(n) = O(nlogn)
```
This is one of the most commonly used algorithm for sorting, to date. It is not a stable alogrithm in the sense that original position of same valued elements may not be retained after sorting. This has a better time complexity than its rival the merge and the heap sort.
For more info please refer the [wikipedia](https://en.wikipedia.org/wiki/Quicksort) page on quick sort.  

Algorithm:
```sh
step 1- choose the highest indexed value as the pivot.
Step 2 − Take two variables to point left and right of the list excluding pivot
Step 3 − left points to the low index
Step 4 − right points to the high
Step 5 − while value at left is less than pivot move right
Step 6 − while value at right is greater than pivot move left
Step 7 − if both step 5 and step 6 does not match swap left and right
Step 8 − if left ≥ right, the point where they met is new pivot
```
Do the above recursively .  
The base case of the recursion is arrays of size zero or one, which never need to be sorted.  

The pivot selection and partitioning steps can be done in several different ways; the choice of specific implementation schemes greatly affects the algorithm's performance, just like selection of interval in Selection sort.  
The crux of the solution lies in selecting the first pivoit point, in this case we are selecting the last element as the pivot, and the next important aspect is the partioning. There are several ways to implement partitioning logic, one such way is described in our implementation.