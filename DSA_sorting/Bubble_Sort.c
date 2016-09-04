# include <stdio.h>
# include <stdbool.h>

# define SIZE 10

int array[SIZE] = {0,9,8,7,6,5,4,3,2,1};

void swap(int arrIdxA){
	int temp = array[arrIdxA];
	array[arrIdxA] = array[arrIdxA + 1];
	array[arrIdxA+1] = temp;
}

void display(){
	printf("\nThe array \n");
	for(int idx = 0;idx < SIZE; idx++){
		printf("%d  ",array[idx]);
	}
}

bool iterate(int size){
	bool flag = false;
	int idx = 0;
	while(idx < size-1){
		if(array[idx] > array[idx+1]){
			swap(idx);
			flag = true;
		}
		idx++;
	}
	return flag;
}



int main(){
	int size = SIZE;
	bool flag = false;
	display();
	while(iterate(size)){
		size--;
	}
	display();
	return 0;
}
