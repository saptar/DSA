# include <stdio.h>
# include <stdlib.h>
# include <stdbool.h>

// utility
void consoleLog(int d){
	printf("\n**********Console logging**************\n");
	printf("%d ",d);
}

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

struct node* minValueNode(struct node* root){
	struct node* currentNode = root;
	if(currentNode == NULL){
		return NULL;
	}
	else{
		while(currentNode -> leftChild != NULL){
			currentNode = currentNode -> leftChild;
		}
		return currentNode;
	}
}

struct node* getParentNode(struct node* node){
	struct node* parentNode = NULL;
	struct node* currentNode = root;
	while(currentNode -> data != node ->data){
		if(currentNode -> data > node -> data){
			parentNode = currentNode;
			currentNode = currentNode -> leftChild;	
		}
		else{
			parentNode = currentNode;
			currentNode = currentNode -> rightChild;
		}
		if(currentNode == NULL){
			return NULL;
		}
	}

	return parentNode;
}

void delete(int data){
	// search for the data and get the parent node of the item to be deleted
	struct node* parentNode  = root;
	// find the node to be deleted
	struct node* nodeToBeDeleted = search(data);
	// case 1 if this is a leaf node, simply delete it.
	if(nodeToBeDeleted -> rightChild == NULL && nodeToBeDeleted ->leftChild == NULL){
		struct node* parentNode = getParentNode(nodeToBeDeleted);
		if(nodeToBeDeleted -> data == parentNode -> leftChild -> data ){
			parentNode -> leftChild = NULL;
		}
		else{
			parentNode -> rightChild = NULL;
		}
		free(nodeToBeDeleted);
	}
	else if(nodeToBeDeleted -> rightChild !=NULL || nodeToBeDeleted -> leftChild !=NULL){
		// case where atleast one child is present
		// check if both child exits
		if(nodeToBeDeleted ->leftChild != NULL && nodeToBeDeleted -> rightChild != NULL){
			// this is the case where there are two childs in the node
			// find the inorder successor node
			struct node* tempNode = minValueNode(nodeToBeDeleted -> rightChild);
			struct node* parentNode = getParentNode(tempNode);
			nodeToBeDeleted -> data = tempNode -> data;
			parentNode -> leftChild = NULL;
			//free(tempNode);
		}
		else{
			// the node has only one child.
			// Find the child copy the child to this node and delete the child node.
			struct node* tempNode = (nodeToBeDeleted ->rightChild !=NULL)? nodeToBeDeleted ->rightChild : nodeToBeDeleted -> leftChild;
			*nodeToBeDeleted = *tempNode;
			free(tempNode);
		}
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
	int array[10] = { 27, 14, 35, 10, 19, 31, 42, 7, 41, 43 };

	for(i = 0; i < 10; i++)
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

	// delete the key 10
	delete(35);  

	printf("\nPreorder traversal: ");
	preOrderTraversal(root);

	printf("\nInorder traversal: ");
	inOrderTraversal(root);

	printf("\nPost order traversal: ");
	postOrderTraversal(root);  
	return 0;
}
