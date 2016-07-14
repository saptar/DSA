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

