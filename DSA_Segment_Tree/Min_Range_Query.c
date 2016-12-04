#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

// utility programs
int getMid(int start, int end){
	return start + (end - start)/2;
}

int getMin(int v1, int v2){
	return (v1 > v2)?v2:v1;
}

// mimimum range query util
int getMinimumUtil(int *st, int ss, int se, int qs, int qe, int si){
	// if the query is in range of the current node 
	// return the value of the node
	if(qs <= ss && qe >= se){
		return st[si];
	}
	if(qs > se || qe < ss){
		// not in range
		return INT_MAX;
	}
	// else if the query range overlaps with some segemnt of the sT
	int mid = getMid(ss, se);
	return getMin(getMinimumUtil(st, ss, mid, qs, qe, 2*si + 1),
		getMinimumUtil(st, mid+1, se, qs, qe, 2*si + 2));
}

int getMinimum(int *st, int n, int qs, int qe){
	// check for errorneous input
	if(qs < 0 || qe > n-1 || qs > qe){
		printf("Invalid input");
		return -1;
	}
	return getMinimumUtil(st, 0, n-1, qs, qe, 0);

}

// segment tree construction util
// arguments: ss -> segment tree starting index
// se -> segment tree ending index
// si -> segment tree present index
// st -> segment tree arr pointer
int constructSTUtil(int arr[], int ss, int se, int *st, int si){
	if(se == ss){
		st[si] = arr[ss];
		return arr[ss];
	}
	// get the mid
	int mid = getMid(ss, se);
	st[si] = getMin(constructSTUtil(arr, ss, mid, st, 2*si + 1),
		constructSTUtil(arr, mid+1, se, st, 2*si + 2));
	return st[si];
}

// construct the segment tree
int *constructST(int arr[], int n){
	// Allocate mem for segment tree array
	int h = (int)(ceil(log2(n)));
	int max_size = 2*(int)pow(2,h) - 1;
	int *st = (int*)malloc(sizeof(int) * max_size);
	constructSTUtil(arr, 0, n-1, st, 0);
	return st;
}

// Driver program
int main(){
	int arr[] = {1, 3, 2, 7, 9, 11};
	int n = sizeof(arr)/sizeof(arr[0]);
	// build segment tree from given array
	int *st = constructST(arr, n);
	int qs = 1; // starting index of the query
	int qe = 5; // ending index of the query
	// print the minimum value in the given array arr[qs...qe]
	printf("The minimum value for range %d , %d is %d\n",qs, qe, getMinimum(st, n, qs, qe));
	return 0;
}