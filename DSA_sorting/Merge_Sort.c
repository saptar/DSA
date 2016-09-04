/**
 * Procedure for merge sort
 * n <- size of the array
 *
 * procdeure mergesort(var a as array)
 * 	if(n == 1)
 * 		return a
 * 	var l1 as an array = a[0]...a[n/2]
 * 	var l2 as an array = a[n/2 + 1]....a[n]
 *
 * 	l1 = mergesort(l1)
 * 	l2 = mergesort(l2)
 *  return merge(l1,l2)
 * End procedure
 *
 * procedure merge(var a as array, var b as array)
 *  var c as array
 *  while(a and b has element)
 *  	if(a[0] > b[0])
 *  		add b[0] to the end of c
 *  		remove b[0] from b
 *  	else
 *  		add a[0] to the end of c
 *  		remove a[0] from a
 *  End while
 *
 * 	while(a has elements)
 * 		add a[ptr] to then end of c
 * 		remove a[ptr] from a
 * 		increment ptr
 * 	End whille
 *
 * 	while(a has elements)
 * 		add a[ptr] to then end of c
 * 		remove a[ptr] from a
 * 		increment ptr
 * 	End whille
 * End procedure
 * 
 */

#include <stdio.h>
#define max 10

int a[10] = { 9,8,7,6,5,4,3,2,1,0 };
int b[10];


void merging(int low, int mid, int high) {
   int l1, l2, i;

   for(l1 = low, l2 = mid + 1, i = low; l1 <= mid && l2 <= high; i++) {
      if(a[l1] <= a[l2])
         b[i] = a[l1++];
      else
         b[i] = a[l2++];
   }

   while(l1 <= mid)    
      b[i++] = a[l1++];

   while(l2 <= high)   
      b[i++] = a[l2++];

   for(i = low; i <= high; i++)
      a[i] = b[i];
}

void sort(int low, int high) {
   int mid;
   
   if(low < high) {
      mid = (low + high) / 2;
      sort(low, mid);
      sort(mid+1, high);
      merging(low, mid, high);
   }else { 
      return;
   }   
}

int main() { 
   int i;

   printf("List before sorting\n");
   
   for(i = 0; i < max; i++)
      printf("%d ", a[i]);
   sort(0, max-1);

   printf("\nList after sorting\n");
   
   for(i = 0; i < max; i++)
      printf("%d ", a[i]);
}