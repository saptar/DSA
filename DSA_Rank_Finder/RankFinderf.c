#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b){
	int temp = *a;
	*a = *b;
	*b = temp; 
}

int standardPartition(int arr[], int l, int r){
	// select the pivot to be the last element
	int pivot = arr[r];
	int i = l;
	for(int j = l; j < r; j++){
		if(arr[j] <= pivot){
			swap(&arr[i], &arr[j]);
			i++;
		}
	}
	swap(&arr[i],&arr[r]);
	return i;
}

int randomisedPartition(int arr[], int l, int r){
	int range = r-l+1;
	int pivot = rand() % range;
	// swap with the last element.
	swap(&arr[l+pivot],&arr[r]);
	return standardPartition(arr, l, r);
}

int kthSmallest(int arr[], int l, int r, int k){
	if(k>0 && k <= r - l + 1){

		int pos = randomisedPartition(arr, l, r);
		if(pos - l == k - 1){
			return arr[pos];
		}
		else if(pos - l > k - 1){
			// the element is in the left sub array
			// recurse on the left sub array
			return kthSmallest(arr, l, pos - 1, k);
		}
		else{
			return kthSmallest(arr, pos+1, r, k - pos + l - 1);
		}
	}
	return INT_MAX;
}

// driver program
int main(){
	int arr[] = {12,3,5,4,7,19,26};
	int n = sizeof(arr)/sizeof(arr[0]);
	int kthsmallest = kthSmallest(arr, 0, n-1, 4);
	printf("\nThe kth smallest element is %d", kthsmallest);
}