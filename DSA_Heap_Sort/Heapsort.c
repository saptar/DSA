#include <stdio.h>
#include <stdlib.h>

struct heap{
	int size;
	int* array;
};

void printArray(int* arr, int size);

// utility function to swap two number
void swap(int* a, int* b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

/**
 * @param struct heap
 * @param int idx
 * @return void
 * description: utility function to take in a presumably malformed binary max heap
 * and correct it to a proper max heap starting from the idx specified.
 * Do it recursively for all child to follow which form a part of the subtree.
 */
void maxHeapify(struct heap* heap, int parent){
	int largest = parent;
	int left = (largest << 1) + 1;
	int right = (largest +1 ) << 1;

	// check if the left child is the largest
	if(left < heap->size && heap -> array[left] > heap -> array[largest]){
		largest = left;
	}
	if(right < heap->size && heap -> array[right] > heap -> array[largest]){
		largest = right;
	}
	if(largest != parent){
		// swap the parent with the largest
		swap(&heap -> array[largest], &heap -> array[parent]);
		// recursive call the lower nodes of the subtree
		maxHeapify(heap, largest);
	}
}

/**
 * @param array int
 * @size int
 * @return struct heap
 * @description: utiltiy function to construct a max heap out of an array of integers with specified size.
 */

struct heap* createAndBuildHeap(int* array, int size){
	struct heap* h = (struct heap*)malloc(sizeof(struct heap));
	if(!h){
		printf("Memory allocation for heap creation failed. Exiting application...");
		exit(-1);
	}
	h->size = size;
	h->array = array; // assign the starting address of the int array.

	// get hold of the right most parent and start heapifying the array
	int parent = (size - 2)/2;
	for(;parent >= 0; parent--){
		maxHeapify(h,parent);
	}
	return h;
}

/**
 * @param array int
 * @param size
 * @return void
 * description: This function takes in an array and returns the sorted form of the array using heapsort
 */
void heapSort(int* array, int size){
	struct heap* heap = createAndBuildHeap(array,size);
	// as per definition of the heap sort,
	// we swap the heap root with the last element of the array
	// modify the new heap and repeat till the size of the heap is 1
	while (heap->size > 1)
    {
        // The largest item in Heap is stored at the root. Replace
        // it with the last item of the heap followed by reducing the
        // size of heap by 1.
        swap(&heap->array[0], &heap->array[heap->size - 1]);
        --heap->size;  // Reduce heap size

        // Finally, heapify the root of tree.
        maxHeapify(heap, 0);
    }
}

// A utility function to print a given array of given size
void printArray(int* arr, int size)
{
    int i;
    for (i = 0; i < size; ++i)
        printf("%d ", arr[i]);
}

// driver function
int main(){
	int arr[] = {12, 11, 13, 5, 6, 7};
    int size = sizeof(arr)/sizeof(arr[0]);
    heapSort(arr,size);
    printf("sorted array is \n");
    printArray(arr,size);
    return 0;
}