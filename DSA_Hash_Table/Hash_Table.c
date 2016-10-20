/**
 * Hash table Data Structure and some basic routines on it.
 * 
 */

# include <stdio.h>
# include <conio.h>
# include <stdlib.h>
# include <stdbool.h>

# define SIZE 20

struct DataItem{
	int key;
	int data;
};

struct DataItem* hashArray[SIZE];
struct DataItem* dummyItem;
struct DataItem* item;

int hashingFunction(int key){
	return key%SIZE;
}

struct DataItem* search(int key){
	// find the hash using hasshing function.
	int hashIndex = hashingFunction(key);
	int idx = 0;
	while(hashArray[hashIndex]!= NULL && hashArray[hashIndex]->key != key){
		// do linear probing 
		++hashIndex;
		++idx;
		// wrap around the array/table
		hashIndex %=SIZE;
		if(idx == SIZE-1)
			break;
	}
	if(idx!=SIZE-1){
		return hashArray[hashIndex];
	}
	else{
		return NULL;
	}

}

void insert(int key, int data){
	// construct the struc
	struct DataItem* item = (struct DataItem*)malloc(sizeof(struct DataItem));
	item -> key = key;
	item -> data = data;
	// generate the hashIndex
	int hashIndex = hashingFunction(key);
	int idx = 0;
	// check if the location is available
	// if yes insert, if no do linear probing till all locations are exhausted.
	while(hashArray[hashIndex] != NULL && hashArray[hashIndex] -> key != -1){
		hashIndex++;
		idx++;
		if(idx == SIZE -1){
			break;
		}
		hashIndex %=SIZE;
	}
	if(idx != SIZE-1){
		hashArray[hashIndex] = item;
	}
	else{
		printf("\nSorry no empty space! Delete an element and try again!");
	}
}

struct DataItem* delete(int key){
	// search the item
	// if present replace the item with a dummyitem whose key = -1
	int hashIndex = hashingFunction(key);
	struct DataItem* deletedItem;
	dummyItem = (struct DataItem*)malloc(sizeof(struct DataItem));
	dummyItem -> key = -1;
	dummyItem -> data = -1;
	if(search(key)!=NULL){
		while(hashArray[hashIndex] -> key != key){
			hashIndex++;
			hashIndex %=SIZE;
		}
		deletedItem = hashArray[hashIndex];
		hashArray[hashIndex] = dummyItem; 
	}
	else{
		return NULL;
	}
	
}

void display(){
	int idx = 0;
	while(idx < SIZE){
		if (hashArray[idx] != NULL){
			printf(" (%d , %d) ",hashArray[idx] -> key, hashArray[idx] -> data);
		}
		else{
			printf(" ~~ ");
		}
		idx++;
	}
	printf("\n\n");
}


int main(){
   

	insert(1, 20);
	insert(2, 70);
	insert(42, 80);
	insert(4, 25);
	insert(12, 44);
	insert(14, 32);
	insert(17, 11);
	insert(13, 78);
	insert(37, 97);

	display();

	item = search(37);

	if(item != NULL){
	  	printf("Element found: %d\n", item->data);
	}else {
	  	printf("Element not found\n");
	}

	if(delete(37) == NULL){
		printf("Element NOT FOUND \n");
	}


	item = search(37);

	if(item != NULL){
	  	printf("Element found: %d\n", item->data);
	}else {
	  	printf("Element not found\n");
	}
}