# include <stdio.h>
# include <stdlib.h>
# include <stdbool.h>

struct node{
	int data;
	struct node* rightChild;
	struct node* leftChild;
};

struct node* root = NULL;

void insert(int data){
	struct node* current;
	struct node* temp = (struct node*)malloc(sizeof(struct node));
	temp -> data = data;
	temp -> rightChild = NULL;
	temp -> leftChild = NULL;
	
	if(root == NULL){
		// start the tree
		root = temp;
	}
	else{
		current = root;
		while(1){
			if(data <= current->data){
				// check if the left node is empty
				if(current -> leftChild != NULL){
					current = current->leftChild;
				}
				else{
					current -> leftChild = temp;
					break;
				}
			}
			else{
				// check if the left node is empty
				if(current -> rightChild != NULL){
					current = current->rightChild;
				}
				else{
					current -> rightChild = temp;
					break;
				}
			}
		}
	}
}

struct node* search(int data){
	struct node* current = root;
	if(current -> data == data){
		return root;
	}
	else{
		while(current -> data != data){
			if(current ->data > data){
				// look to the left
				current = current -> leftChild;
			}
			else{
				current = current -> rightChild;
			}
			if(current == NULL){
				return NULL;
			}
		}
		return current;
	}
}

void preOrderTraversal(struct node* node){
	if(node!=NULL){
		printf("%d ",node -> data);
		preOrderTraversal(node -> leftChild);
		preOrderTraversal(node -> rightChild);
	}
}
void inOrderTraversal(struct node* node){
	if(node!=NULL){
		inOrderTraversal(node -> leftChild);
		printf("%d ", node -> data);
		inOrderTraversal(node -> rightChild);
	}
}
void postOrderTraversal(struct node* node){
	if(node!=NULL){
		postOrderTraversal(node -> leftChild);
		postOrderTraversal(node -> rightChild);
		printf("%d ", node -> data);
	}
}

// driver program
int main(){
	int i;
	int array[7] = { 27, 14, 35, 10, 19, 31, 42 };

	for(i = 0; i < 7; i++)
	  insert(array[i]);

	i = 31;
	struct node * temp = search(i);

	if(temp != NULL) {
	  printf("[%d] Element found.", temp->data);
	  printf("\n");
	}else {
	  printf("[ x ] Element not found (%d).\n", i);
	}

	i = 15;
	temp = search(i);

	if(temp != NULL) {
	  printf("[%d] Element found.", temp->data);
	  printf("\n");
	}else {
	  printf("[ x ] Element not found (%d).\n", i);
	}   

	printf("\nPreorder traversal: ");
	preOrderTraversal(root);

	printf("\nInorder traversal: ");
	inOrderTraversal(root);

	printf("\nPost order traversal: ");
	postOrderTraversal(root);  
	return 0;
}
