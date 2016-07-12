/**
 * psuedo code for interpolation search.
 *
 * A -> the sorted and equally distributed array
 * N -> the size of the array
 * X -> value to be searched
 *
 * procedure interpolation_search
 *
 * 	set Lo -> 0
 * 	set Hi -> n-1
 * 	set mid -> -1
 *
 * 	while X does not match
 * 		if Lo == Hi or A[Lo] == A[Hi]
 * 			Exit: X not found
 * 		end if
 * 		set Mid = Lo + ((Hi-Lo)/(A[Hi]-A[Lo]))*(X-A[Lo])
 * 		if A[mid] == X
 * 			Exit: X found
 * 		Else
 * 			if A[mid] < X
 * 				Lo = Mid + 1
 * 			els if A[mid] > X
 * 				Hi = Mid -1
 * 			end if
 * 		end if
 * 	End While
 */
# include <stdio.h>
# include <time.h>
# include <math.h>

# define SIZE 10

 int interpolation_search(double Array[], double searchTerm, double lowerBound, double upperBound){
 	double midpoint;
 	long int mid;
 	int flag=0;
 	if(upperBound < lowerBound || Array[(int)upperBound] == Array[(int)lowerBound]){
 		flag = 0;
 		return flag;
 	}
 	midpoint = lowerBound + (((double)(upperBound - lowerBound) / (Array[(int)upperBound] - Array[(int)lowerBound])) * 
 				(searchTerm - Array[(int)lowerBound]));
 	mid = (long int) midpoint;
 	printf("\n midpoint : %ld",mid);
 	if(Array[mid] == searchTerm){
 		
 		flag = 1;
 		return flag;
 	}
 	else if(Array[mid] < searchTerm){
 		// increment the lowerBound
 		lowerBound = mid + 1;
 		return interpolation_search(Array, searchTerm, lowerBound , upperBound);
 	}
 	else{
 		// update the upper bound
 		upperBound = mid - 1;
 		return interpolation_search(Array, searchTerm, lowerBound, upperBound);
 	}


 }

 int main(){
 	double Array[SIZE] = {1,3,5,11,35,53,60,67,88,90};;
 	double size = SIZE;
 	double lowerBound = 0;
 	double upperBound = size - 1;
 	double searchTerm = 67;
 	int c = 0; 
 	clock_t begin = clock();
 	c = interpolation_search(Array,searchTerm,lowerBound,upperBound);
 	

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