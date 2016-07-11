/**
 * Algorithm for binary sort
 *
 * procdure binary_sort
 * A <- Sorted Array
 * n <- size of the array
 * x <- value to search in the array
 *
 * set lowerBound = 0
 * set upperBound = n
 *
 * while x not found repeat
 * 	if upperBound < lowerBound
 * 	 Exit: x does not exits
 *
 * 	set midpoint  = lowerbound + (upperBound-lowerBound)/2
 *
 * 	if A[midpoint] == x
 *   Exit : x found at midpoint
 *  if A[midpoint] < x
 *   set lowerBound  = midpoint + 1
 *  if A[midpoint] > x
 *   setf upperBound = midpoint - 1
 *
 * End while
 */

# include <stdio.h>
# include <time.h>

# define SIZE 100000

 int binary_search(double Array[], double searchTerm, double lowerBound, double upperBound){
 	long int midpoint;
 	int flag=0;
 	if(upperBound < lowerBound){
 		flag = 0;
 		return flag;
 	}
 	midpoint = lowerBound + (upperBound-lowerBound)/2;
 	if(Array[midpoint] == searchTerm){
 		
 		flag = 1;
 		return flag;
 	}
 	else if(Array[midpoint] < searchTerm){
 		// increment the lowerBound
 		lowerBound = midpoint + 1;
 		return binary_search(Array, searchTerm, lowerBound , upperBound);
 	}
 	else{
 		// update the upper bound
 		upperBound = midpoint - 1;
 		return binary_search(Array, searchTerm, lowerBound, upperBound);
 	}


 }

 int main(){
 	double Array[SIZE];
 	double size = SIZE;
 	double lowerBound = 0;
 	double upperBound = size - 1;
 	double searchTerm = size-1;
 	int c = 0;
 	for(long int i = 0; i < SIZE ; i++){
 		Array[i] = i;
 	}
 	clock_t begin = clock();
 	c = binary_search(Array,searchTerm,lowerBound,upperBound);
 	

	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	if(c == 0){
 		printf("\nsearch term NOT FOUND\n");
 	}
 	if(c == 1){
 		printf("\nsearch term FOUND\n");
 	}
 	printf("\noperation complete in %lf\n", time_spent);

 }