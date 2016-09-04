/*
input : stack /array of fixed MAXSIZE
problem : to implement various stack routines on the input.
*/

# include <stdio.h>
# include <stdbool.h>

int MAXSIZE = 8; // size of the stack
int stack[8];
int top = -1;

// find out if the stack is empty

bool isEmpty(){
	bool isEmpty = false;
	if(top == -1){
		isEmpty = true;
	}
	return isEmpty;
}

// find out if the stack is full

bool isFull(){
	bool isFull = false;
	if(top == MAXSIZE){
		isFull = true;
	}
	return isFull;
}

// peek : return the top of the stack with out changing the top pointer

int peek(){
	return stack[top];
}

// push : add an element to the top of the array. 
// set the top to point to the new item

bool push(int item){
	if(isFull() == true){
		printf("\n The stack is already full cannot add any more item.");
		return false;
	}
	top = top + 1;
	stack[top] = item;
	return true;
}

// pop : get the top element out and decrement the top pointer
int pop(){
	if(isEmpty() == true){
		printf("\n The stack is empty");
		return NULL;
	}
	int popedItem = stack[top];
	top -=1;
	return popedItem;
}

// printStack : print stack
bool printStack(){
	if(isEmpty() == true){
		printf("\n The stack is empty");
		return false;
	}
	int idx;
	printf("[");
	for(idx = 0 ; idx <= top ; idx++ ){
		printf("%d \t",stack[idx]);
	}
	printf("]");
	return true;
}


int main(){
	push(1);
	push(2);
	push(3);
	push(4);
	push(5);
	push(7);
	push(8);
	push(9);

	printStack();

	// pop the stack
	printf("\nThe stacked poped \n [");
	while(top != -1){
		printf("%d\n", pop());
	}
	printf("]");
	return 0;
}