#include <stdio.h>
#include <stdlib.h>

struct heap{
	int size;
	int count;
	int *heaparr;
};

int* heap;
int size, count;
int initial_size = 4;

void heap_display(struct heap* heap);


void heap_init(struct heap* h){
	h->count  = 0;
	h->size = initial_size;
	h->heaparr = (int*)malloc(sizeof(int) * initial_size);
	if(!h->heaparr){
		printf("Error allocating memory...\n");
		exit(-1);
	}
}

void max_heapify(int* data, int loc, int count){
	int left, right, largest, temp;
	left = 2*loc + 1;
	right = left + 1;
	largest = loc;

	if(left <= count && data[left] > data[largest]){
		// the left child is larger than parent
		// swap
		largest = left;
	}
	if(right <= count && data[right]> data[largest]){
		largest = right;
	}
	if(largest != loc){
		temp = data[loc];
		data[loc] = data[largest];
		data[largest] = temp;
		max_heapify(data, largest, count);
	}
}

void heap_push(struct heap* h, int value){
	int index, parent;
	// resize the heap if it is too small to hold the new data
	if(h->count == h->size){
		h->size +=1;
		h->heaparr = (int*)realloc(h->heaparr, sizeof(int) * h->size);
		if(!h->heaparr){
			printf("Failed to allocate additional memory...\n");
			exit(-1);
		}
	}
	// add the new value to the last index
	index = h->count++;
	// find out where to put the element and put it
	for(;index;index = parent){
		parent = (index -1)/2;
		if(h->heaparr[parent] >= value){
			break;
		}
		h->heaparr[index] = h->heaparr[parent];
	}
	h->heaparr[index] = value;
	heap_display(h);
}


void heap_display(struct heap* heap){
	int i;
	for(i=0;i<heap->count;i++){
		printf("|%d|", heap->heaparr[i]);
	}
	printf("\tCount  %d and Size %d\n",heap->count, heap->size);
}

int heap_delete(struct heap* h){
	int removed;
	h->count -=1;
	int temp = h->heaparr[h->count];

	if(h->count <= (h->size+2) && h->size > initial_size){
		h->size -=1;
		h->heaparr =(int *) realloc(h->heaparr, sizeof(int) * h->size);
		if(!h->heaparr)exit(-1);
	}
	removed = h->heaparr[0];
	h->heaparr[0] = temp;
	max_heapify(h->heaparr, 0, h->count);
	return removed;
}

int emptyPQ(struct heap* heap){
	int i;
	while(heap->count !=0){
		printf("\nheap delete %d",heap_delete(heap));
	}
}

// driver program
int main(){
	struct heap h;
	heap_init(&h);
	heap_push(&h,1);
	heap_push(&h,5);
	heap_push(&h,3);
	heap_push(&h,7);
	heap_push(&h,9);
	heap_push(&h,8);
	heap_display(&h);
	emptyPQ(&h);
	return 0;
}