/*
input : Simple linked list 
problem : to display the list; insert a node at the fisrt location,
delete a node in the first location, given a key find a node, sort the linked list and reverse the linked list.
Assumption: key and value are the data contained with in each link/node/

*/

# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <stdbool.h>

// declare individual links

struct node {
	int data;
	int key;
	struct node *next; // pointer to the next link/node
};


// pointer to the head and the current link
struct node *head = NULL;
struct node *current = NULL;

// display the list

void printList(){
	struct node *ptr = head;
	printf("\n[");
	while(ptr != NULL){
		printf("(%d, %d)",ptr->key, ptr->data);
		ptr = ptr->next;
	}
	printf("]\n");
}

// insert list at the first location

void insertFirst(int key, int value){
	struct node *first = (struct node*) malloc(sizeof (struct node));
	first->key = key;
	first->data = value;
	// point the next pointer to the previous head
	first->next = head;
	// the head now points to the newly created link
	head = first ;
}

// delete link at the first location and return the deleted node

struct node* deleteFirst(){
	// save reference to the first node
	struct node* tempReference = head;
	// make the next element as the head
	head = head ->next;
	return tempReference;
}

// isList empty

bool isEmpty(){
	return head == NULL;
}

// lenght of the list

int length(){
	int lenghtOfList = 0;
	struct node *current = NULL;
	for (current = head; current != NULL; current = current->next){
		lenghtOfList +=1;
	}
	return lenghtOfList;
}

// find a link with given key

struct node* find(int key){
	// take current to head
	current = head;
	// while current -> next != NULL
	// check current -> key == key
	// return current
	if (current == NULL){
		return NULL;
	}
	while (current -> next !=NULL){
		if (current -> key == key){
			break;
		}
		current = current ->next;
	}
	return current;
}

// delete a node with a given key

struct node* deleteNode(int key){
	// find the node using the key.
	// make that the current and set previousToCurrent with the previous node.
	// save reference of the current next
	// set previousToCurrent with the saved reference

	current = find(key);
	if(current == NULL){
		return NULL;
	}
	if(current == head){
		return  deleteFirst();
	}
	struct node* previousToCurrent = head;
	while(previousToCurrent->next !=current && previousToCurrent != current){
		previousToCurrent= previousToCurrent->next;
	}
	previousToCurrent->next = current->next;
	return current;
}

// sort the linked list
// use bubble sort.

void sort(){
	int i, j, k, tempData, tempKey;
	struct node *current, *next;
	int size = length();
	k = size;

	// every iteration of the outer for loop would get the largest link to the exterme right/end.

	for(i = 0; i< size-1 ; i++, k--){
		current = head;
		next = current->next;
		// every iteration of the 
		for(j=1; j<k ; j++){
			// number of comparision is one less than total number of elements.
			// hence j starts from 1.
			if(current->data > next->data){
				//swap the links
				tempData = current->data;
				tempKey = current->key;
				current->data = next->data;
				current->key = next->key;
				next->data = tempData;
				next->key = tempKey;
			}
			current = current ->next;
			next = next->next;
		}
	}
}

// reverse the linked list

void reverse(){
	struct node *prev = NULL;
	struct node *current  = head;
	struct node *next ;
	while(current!=NULL){
		next = current -> next;
		current->next = prev;
		prev = current;
		current = next;	
	}


	head = prev;
}

int main(){
	insertFirst(1,10);
	insertFirst(2,20);
	insertFirst(3,60);
	insertFirst(4,90);
	insertFirst(5,0);
	insertFirst(6,600);
	insertFirst(7,70);

	printList();

	struct node* deletedItem = deleteFirst();
	if(deletedItem != NULL)
	printf("delete node is %d, %d", deletedItem->key,deletedItem->data);

	printList();
	struct node *returnedLink = find(1);
	printf("returned node is %d, %d \n", returnedLink->key,returnedLink->data);

	struct node* deletedItemUsingKey = deleteNode(6);
	if(deletedItemUsingKey !=NULL)
	printf("delete node is %d, %d \n", deletedItemUsingKey->key,deletedItemUsingKey->data);
	printList();
	sort();
	reverse();
	printList();



	return 0;
}