/* 
 * Input : Array of size n and insertion has to be made at position k where k<=N
 * Algorithm for Insertion sort
 * 1. START
 * 2. set J=N
 * 3. set N=N+1
 * 4. Repeat step 5 and 6 until J>=k
 * 5. set Array[J+1] = Array[J]
 * 6. set J=J-1
 * 7. set Array[k] = ITEM to be inserted
 * 8. END
 *
 */


# include <stdio.h>
# include <conio.h>


int main(){
	int array[] = {1,2,3,4,5};
	int size = 5 ; // size of the array
	int position = 3 ; // position where item to be inserted
	int item = 10 ;  // new item to be inserted
	int i = 0 , j = 0;
	// print out the original array
	printf("Item in the array\n");
	for (i=0; i< size; i++){

		printf("%d\n",array[i]);
	}
	printf("Item in the inserted array \n");
	j = size;
	size = size+1;
	while(j>=position){
		array[j+1]= array[j];
		j-=1;
	}
	array[position] = item;
	for (i=0; i< size; i++){

		printf("%d\n",array[i]);
	}
	return 0;
}