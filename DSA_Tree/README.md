## Tree Data Structure

Tree represents nodes connected by edges. We are going to learn binary tree or binary search tree specifically.  
Binary tree is a special data structure used for storage purposes. A binary tree has special condition in that, each node can have two children at maximum. A binary tree have benifits of both an ordered array and linked list as search is as quick as a sorted array and insertion or deletion is as fast as a linked list.  

### Terminologies
Following are important terms with respect to a tree:  
- Path - Refers to sequence of nodes along the edges.  
- Root - Node at the top of the tree is called root. There is only one root per tree and one path from root node to any node.  
- Parent - Any node except root node has one path upward to a node called parent node of that node.  
- Child - Node below a given node connected path a path from the given node downwards is called the child node of that node.  
- Leaf - Node which does not have any child node is called as a leaf node of the tree.  
- Subtree - Subtree represents decendant of a node.  
- Visiting - Refers to checking value of a node when the control is on that node.  
- Traversing - Traversing means passing through a node in a specific order.  
- Levels - Level of a node represents the generation of the node.  
- Keys - Key represent a value of a node based on which a search operation is to be carried out.  

### Binary Search Tree (BST) representation.  
Binary search tree represnts a special behaviour. The node's left child must have value less than that of the node and the right node must have value greater than that of the node. A tree node must have a structure as follows:  
```sh
struct node{
	int data;
	struct node* rightChild;
	struct node* leftChild;
}
```
All tree node shares common structure.

### BST basic operations

The basic operation that can be performed on a binary tree data structure:  
- Insert - insert an element in a tree/ create a tree.  
- Search - search an element in a tree.  
- pre-order traversal - traverse a tree in a pre-ordered manner.      
- post-order traversal - traverse a tree in post order manner.  
- in-order traversal - traverse a tree in an in-order manner.  

### Insert
The very first insertion creates the tree. Afterwards, whenever an element is to be inserted, first locate its proper location . Start search from root node and then if data value is less than key value, search empty location in the left of subtree and insert data , otherwise search a location in the right side.  
Algorithm:  
```sh
If root is NULL 
   then create root node
return

If root exists then
   compare the data with node.data
   
   while until insertion position is located

      If data is greater than node.data
         goto right subtree
      else
         goto left subtree

   endwhile 
   
   insert data
	
end If
```

### Search Operation
Whenever an element is to be searched in a tree, start from the root node. Then if the value is less than the key value search in the left subtree otherwise look in the right subtree. Do same for all nodes encountered.  
Algorithm:  
```sh
If root.data is equal to search.data
   return root
else
   while data not found

      If data is greater than node.data
         goto right subtree
      else
         goto left subtree
         
      If data found
         return node

   endwhile 
   
   return data not found
   
end if    
```

### Delete operations:  

There are three posible cases that we can encounter while deleting a node.  
- **Node to be deleted is a leaf node**  
	In such a case, find the node and simply delete the node.  
	```sh
	          50                            50
           /     \         delete(20)      /   \
          30      70       --------->    30     70 
         /  \    /  \                     \    /  \ 
       20   40  60   80                   40  60   80
	```  
- **Node to be deleted has one child**  
	Copy the child to the node and delete the child.  
	```sh
	 		  50                            50
           /     \         delete(30)      /   \
          30      70       --------->    40     70 
            \    /  \                          /  \ 
            40  60   80                       60   80
	```  
- **Node to be deleted has two children**  
	In such a case, find the inorder successor of the node and copy that to the node and delete the inorder successor.  
	```sh
	          50                            60
           /     \         delete(50)      /   \
          40      70       --------->    40    70 
                 /  \                            \ 
                60   80                           80
	```
	Inorder successor is need only when the node to be deleted has a right child.  

### Tree Traversal  
Traversal is a process of visiting all the nodes of a tree and may print their values. We cannot access nodes in a tree radomly.  
As mentioned above there are three types of traversal and they are:  
- **Inorder Traversal**  
	In this method the left subtree is visited first and then the root followed by the right subtree.
	Consider the following binary tree  
	```sh

								A <- Root
							   / \
							  /   \
							 B     C
					Right->	/ \   / \ <- Left subtree
						   D   E F   G

	```
	We start from **A**, and following in-order traversal , we move to its left subtree **B**. **B** is also traversed in order , and the process goes on untill all the nodes are visited. The output of in-order traversal of the mentioned tree will be  
	```sh
	D -> B -> E -> A -> F -> C -> G
	```
	Algorithm:  
	```sh
	Until all nodes are traversed −
		Step 1 − Recursively traverse left subtree.
		Step 2 − Visit root node.
		Step 3 − Recursively traverse right subtree.
	```
  
- **Pre-order Traversal**  
	In this method the root node is visited first then the left subtree and then the right subtree.  
		Consider the following binary tree  
	```sh

								A <- Root
							   / \
							  /   \
							 B     C
					Right->	/ \   / \ <- Left subtree
						   D   E F   G

	```
	We start from **A**, and following pre-order traversal, we first visit **A** itself , before moving on to **B** and visiting it. We do the same with the subtree rooted at **B**, before moving on with **C**.  
	```sh
	A -> B -> D -> E -> C -> F -> G
	```
	Algorithm:  
	```sh
	Until all nodes are traversed −
		Step 1 − Visit root node.
		Step 2 − Recursively traverse left subtree.
		Step 3 − Recursively traverse right subtree.
	```
  
- **Post-order Traversal**  
	In this traversal method, the root node is visited last, hence the name. First we traverse left subtree, then right subtree and finally root.  
	```sh

								A <- Root
							   / \
							  /   \
							 B     C
					Right->	/ \   / \ <- Left subtree
						   D   E F   G

	```
	We start from **A**, and following pre-order traversal, we first visit left subtree **B**. **B** is also traversed post-ordered. And the process goes on until all the nodes are visited. The output of post-order traversal of this tree will be  
	```sh
	D -> E -> B -> F -> G -> C -> A
	```
	Algorithm:  
	```sh
	Until all nodes are traversed −
		Step 1 − Recursively traverse left subtree.
		Step 2 − Recursively traverse right subtree.
		Step 3 − Visit root node.
	```


