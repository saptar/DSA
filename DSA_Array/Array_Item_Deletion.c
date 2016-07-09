/*
Assumption: Array is of n and item to be delete is at index k <= n
Algorithm:
1. Start
2. set j= k
3. size = size-1
4. repeat step 5 and 6 while j<=size
5. 
*/
# include <stdio.h>
# include <conio.h>

int main(){
	int array[]={1,2,3,4,5,6};
	int position = 4; // 0 based
	int size = 6;
	int i=0,j=0;
	// print the original array
	printf("Array elements are \n");
	for (i=0;i<size;i++){
		printf("%d\n",array[i]);
	}
	j= position;
	size = size-1;
	while(j<=size){
		array[j]=array[j+1];
		j= j+1;
	}
	
	// print the reduced array
	printf("Items in the reduced array \n");
	printf("Array elements are \n");
	for (i=0;i<size;i++){
		printf("%d\n",array[i]);
	}
}