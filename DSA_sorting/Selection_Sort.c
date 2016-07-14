# include <stdio.h>

# define SIZE 10

int array[SIZE] = {9,8,7,6,5,4,3,2,1,0};

void select(int array[], int selectedIndex){
	int currentSelectionIdx, temp;

	if(selectedIndex < SIZE-1){
		select(array, selectedIndex + 1);
		currentSelectionIdx = selectedIndex;
		while(selectedIndex < SIZE-1 ){
			if(array[currentSelectionIdx] > array[selectedIndex+1]){
				temp = array[selectedIndex];
				array[selectedIndex] = array[selectedIndex+1];
				array[selectedIndex+1] = temp;	
			}
			selectedIndex++;
		}
	}


}

void display(){
	printf("\nArray\n");
	for(int i=0;i<SIZE;i++){
		printf("%d  ", array[i]);
	}
}

int main(){
	int idx = 0;
	display();
	printf("\nAfter Sorting\n");
	while(idx < SIZE){
		select(array,0);
		idx ++;
	}
	display();
}