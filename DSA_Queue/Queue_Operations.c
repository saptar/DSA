# include <stdio.h>
# include <stdbool.h>
# include <stdlib.h>
# include <string.h>

# define MAX 6

int intArray[MAX];
int rear = -1;
int front = 0;
int itemCount = 0;

// peek 
int peek(){
	return intArray[front];
}
 // isFull
 bool isFull(){
 	return itemCount == MAX;
 }

 // isEmpty
 bool isEmpty(){
 	return itemCount == 0;
 }

 // enqueue
 // enqueue is implemented by incrementing the rear pointer
 // and then adding the new item in the rear pointer index.

 void enqueue(int item){
 	if(!isFull()){
 		if(rear == MAX -1){
 			// this is the case when we need to add a new element 
 			// when the rear pointer is at MAX-1 and the front pointer is at 1
 			// this is due to the fixed size of the array.
 			// we cannot go beyond MAX size .
 			rear = -1;
 		}
 		intArray[++rear] = item;
 		itemCount++;
 	}

 }
 int dequeue(){
   int data = intArray[front++];
	
   if(front == MAX){
      front = 0;
   }
	
   itemCount--;
   return data; 
}

 int main() {
   /* insert 5 items */
   enqueue(3);
   enqueue(5);
   enqueue(9);
   enqueue(1);
   enqueue(12);

   // front : 0
   // rear  : 4
   // ------------------
   // index : 0 1 2 3 4 
   // ------------------
   // queue : 3 5 9 1 12
   enqueue(15);

   // front : 0
   // rear  : 5
   // ---------------------
   // index : 0 1 2 3 4  5 
   // ---------------------
   // queue : 3 5 9 1 12 15
	
   if(isFull()){
      printf("Queue is full!\n");   
   }

   // remove one item 
   int num = dequeue();
	
   printf("Element removed: %d\n",num);
   // front : 1
   // rear  : 5
   // -------------------
   // index : 1 2 3 4  5
   // -------------------
   // queue : 5 9 1 12 15

   // insert more items
   enqueue(16);

   // front : 1
   // rear  : -1
   // ----------------------
   // index : 0  1 2 3 4  5
   // ----------------------
   // queue : 16 5 9 1 12 15

   // As queue is full, elements will not be inserted. 
   enqueue(17);
   enqueue(18);

   // ----------------------
   // index : 0  1 2 3 4  5
   // ----------------------
   // queue : 16 5 9 1 12 15
   printf("Element at front: %d\n",peek());

   printf("----------------------\n");
   printf("index : 5 4 3 2  1  0\n");
   printf("----------------------\n");
   printf("Queue:  ");
	
   while(!isEmpty()){
      int n = dequeue();           
      printf("%d ",n);
   }   
}