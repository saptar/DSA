# include <stdio.h>
# include <stdbool.h>

# define SIZE 10

int array[SIZE] = {9,8,7,6,5,4,3,2,1,0};

void swap(int* a, int* b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

/**
 * This function takes the last element as the pivot.
 * Places the pivot value in the right postion in the sorted array.
 * All the values that are smaller than the pivot element are placed to the left and
 * all the values that are greater than the pivot are placed towards the right of the pivot element.
 */

int partioning(int arr[], int low, int high){
	int pivot = arr[high]; // the last element in the array
	int i = (low-1); // this will be incremented and used for swapping

	for (int j=low; j< high;j++){
		// if current element is smaller than equal to pivot
		if(arr[j] <= pivot){
			++i;
			// swap the current element and ith element.
			swap(&arr[i],&arr[j]);
		}
	}
	swap(&arr[i+1],&arr[high]);
	return (i + 1);
}


void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        int pi = partioning(arr, low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void display(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
	int n = SIZE;
	display(array,n);
    quickSort(array, 0, n-1);
    printf("Sorted array: \n");
    display(array, n);
    return 0;
}