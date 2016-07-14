/**
 * Here we will be using a recursion to implement insertion sort.
 * As a rule of thumb , any logic which can be written down using a while condtional statement
 * Can invariably be represented in form of recursion.
 *
 * Here in this case, the kth step of recursion(last recursion) would have index 0 and 1
 * We need to sort this and return to (k-1)th step as sorted sub array and so on till we move to the first call of recursion.
 * Print the array and it shoud be sorted.
 */


# include <stdio.h>

# define SIZE 10

int array[SIZE] = {9,8,7,6,5,4,3,2,1,0};

void insert(int array[], int index){
	int idx, temp;
	if(index>0){
		insert(array, index-1); // returns sorted sub-array
		temp = array[index]; // to be inserted
		idx = index -1;
		while(idx >= 0 && array[idx] > temp){
			// shift
			array[idx+1] = array[idx];
			idx--;
		}
		// insert
		array[idx+1] = temp;
	}
}

void display(){
	printf("\nPrint Array\n");
	for(int i=0;i<SIZE;i++){
		printf("%d  ",array[i]);
	}
}

int main(){
	display();
	insert(array, SIZE-1);
	printf("\nAfter sorting");
	display();
	return 0;
}