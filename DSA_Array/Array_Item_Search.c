/*
Input : Linear array with n elements 
Problem: To find the element 'Item' in the array , if it exist, if not return -1
Algorithm:
1. Start
2. Set j=0 and Flag = false
3. Repeat step 4 and 5 while j<n
4. if array[j] == item
5. goto 7
6. j=j+1
7. flag = true
8. if flag == true
9. print j and item
10. if flag != true
11. print -1
12. Stop.

*/

# include <stdio.h>

typedef enum { false, true } bool;

int main(){
	int array[]={1,2,3,4,5,6,7,8,9};
	int item = 5;
	int size = 9;
	int j = 0, i=0;
	bool flag = false;
	// print the original array
	printf("The elements in the array are \n");
	for(i=0 ;i<size;i++){
		printf("%d\n", array[i]);
	}
	// print the index if item present or print -1
	while(j<size){
		if(array[j]== item){
			flag = true;
			break;
		}
		j+=1;
	}
	if(flag == true){
		printf("item %d is present in index %d\n",item,j );
	}
	else{
		printf("-1");
	}
	return 0;
}