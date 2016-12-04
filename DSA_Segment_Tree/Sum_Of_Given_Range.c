#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// declaring function to calculate the mid
int getMid(int ss, int se);

// updateValueUtil
void updateValueUtil(int *st, int ss, int se, int i, int diff, int si){
	// check if the input index lies outside the range
	// base case of recursion
	if(i < ss || i > se){
		return;
	}
	// if input index is in range of this node
	// update this node and its children.
	st[si] = st[si] + diff;
	if(se != ss){
		int mid = getMid(ss, se);
		updateValueUtil(st, ss, mid, i, diff, 2*si + 1);
		updateValueUtil(st, mid+1, se, i, diff, 2*si + 2);
	}
}

// update value
// The fuction to update the value in input array and segment tree.
void updateValue(int arr[], int *st, int n, int i, int new_value){
	// check for errornous input
	if(i < 0 || i > n-1){
		printf("Invalid input");
		return ;
	}
	// get difference betweeen the old value and the new value
	int diff = new_value - arr[i];
	// update the value in the input array
	arr[i] = new_value;
	updateValueUtil(st, 0, n-1, i, diff, 0);
}

// getSumUtil
int getSumUtil(int *st, int ss, int se, int qs, int qe, int si){
	if(qs <= ss && qe >= se){
		return st[si];
	}
	if(se < qs || ss > qe){
		return 0;
	}
	// if part of this segment overlaps with the given range
	int mid = getMid(ss, se);
	return getSumUtil(st, ss, mid, qs, qe, 2*si+1) + getSumUtil(st, mid+1, se, qs, qe, 2*si+2);
}

// Return sum of element in the range querystart(qs) to queryend(qe).
// It maily uses getSumUtil()
int getSum(int *st, int n, int qs, int qe){
	// check for erronous input values
	if(qs < 0 || qe > n-1 || qs > qe){
		printf("Invalid input");
		return -1;
	}
	return getSumUtil(st, 0, n-1, qs, qe, 0);
}

// utility function to get the mid of two numbers
int getMid(int ss, int se){
	return ss + (se - ss)/2;
}

// A recursive function that constructs a st for array [ss ... se]
// st -> segment tree
// ss -> array starting index
// se -> array ending index
// si -> node index
int constructSTUtil(int arr[], int ss, int se, int *st, int si){
	// if there is one element in the array
	// store it in the current node of the st
	// this is also the base case of recursion.
	if(se == ss){
		st[si] = arr[ss];
		return arr[ss];
	}
	// if there is more than one element then recur for right and left
	// subtree and store the sum of the values in this node
	int mid = getMid(ss, se);
	st[si] = constructSTUtil(arr, ss, mid, st, (2*si)+1) + constructSTUtil(arr, mid+1, se, st, (2*si)+2);
	return st[si];
}

// construct segement tree
int *constructST(int arr[], int n){
	// Allocates mememory for the segment tree array
	// Height of the array
	int h = (int)(ceil(log2(n)));
	// Maximum size of the segment tree
	int max_size = 2*(int)pow(2, h) - 1;
	// Allocate memory
	int *st = (int*) malloc(sizeof(int) * max_size);
	// Fill the allocated mem ref to by st
	constructSTUtil(arr, 0, n-1, st, 0);

	return st;
}

//Driver program for the program
int main(){
	int arr[] = {1,3,5,7,9,11};
	int n = sizeof(arr)/sizeof(arr[0]);
	// Build the segment tree from given array
	int *st = constructST(arr, n);
	// Print the sum of values in the array from index 1 to 3.
	printf("sum of values in the given range = %d\n",getSum(st, n, 1, 3) );
	// update: arr[1] = 10
	updateValue(arr, st, n, 1, 10);
	// Find the sum after the index value has been updated
	printf("sum after updation = %d\n",getSum(st, n, 1, 3));
}