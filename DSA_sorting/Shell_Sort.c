# include <stdio.h>

# define SIZE 10

int array[] = {9,8,7,6,5,4,3,2,1,0};


void display(){
	printf("Array\n");
	for(int i = 0; i < SIZE; i++){
		printf("%d ",array[i]);
	}
	printf("\n");
}


void shellsort(){
	int inner, outer;
	int valueToInsert;
	int interval;
	int elements = SIZE;

	while(interval <= elements/3){
		interval = 3 * interval + 1;
	}
	while(interval > 0){

		for(outer = interval; outer < elements ; outer++){
			valueToInsert = array[outer];
			inner = outer;

			while(inner > interval-1 && array[inner-interval]>=valueToInsert){
				array[inner] = array[inner-interval];
				inner -=interval;
				printf(" item moved %d \n", array[inner]);
			}
			array[inner] = valueToInsert;
			printf(" item inserted at position : %d , valued : %d", inner, valueToInsert);
		}
		interval = (interval-1)/3;
	}
}

int main() {
   printf("\nInput Array: ");
   display();
 
   shellsort();
   printf("\nOutput Array: ");
   display();

   return 1;
}